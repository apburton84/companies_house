#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .companies_house import CompaniesHouse
import json


class CompanyOwnership:
    def __init__(self, api_key):
        self.api = CompaniesHouse(api_key=api_key)

    def extract(self, json, company_number):
        json_extract = []
        if "items" in json:
            for i in json["items"]:
                if "identification" in i:
                    json_extract.append(
                        self.extract_indent(i["identification"], company_number)
                    )

        return json_extract

    def extract_indent(self, ident, company_number):
        ident_dict = {"parent_company": company_number}

        if "registration_number" in ident:
            ident_dict["child_company"] = ident["registration_number"].upper()

        if "identification_type" in ident:
            ident_dict["identification_type"] = ident["identification_type"].upper()

        if "legal_form" in ident:
            ident_dict["legal_form"] = ident["legal_form"].upper()

        if "place_registered" in ident:
            ident_dict["place_registered"] = ident["place_registered"].upper()

        if "legal_authority" in ident:
            ident_dict["legal_authority"] = ident["legal_authority"].upper()

        return ident_dict

    def get_officers(self, company_number):
        return self.extract(self.api.officers(company_number).json(), company_number)

    def get_persons_with_significant_control_list(self, company_number):
        try:
            return self.extract(
                self.api.persons_with_significant_control_list(company_number).json(),
                company_number,
            )
        except json.decoder.JSONDecodeError:
            return []

    def fetch(self, company_number):
        officers = self.get_officers(company_number)
        pwsc = self.get_persons_with_significant_control_list(company_number)

        entities = [*officers, *pwsc]

        for i in entities:
            print(i["parent_company"], i["child_company"])

            officers = self.get_officers(i["child_company"])
            pwsc = self.get_persons_with_significant_control_list(i["child_company"])

            for j in [*officers, *pwsc]:
                entities.append(j)

        return entities
