"""Companies House API wrapper"""
import requests


class CompaniesHouse:
    """Companies House API wrapper"""

    def __init__(self, api_key=""):
        """Initialize the Companies House API wrapper"""
        self.api_key = api_key
        self.api_endpoint = "api.company-information.service.gov.uk"

    def _http_get_request(self, endpoint):
        session = requests.Session()
        session.auth = (self.api_key + ":", "")

        return session.get("https://" + self.api_endpoint + endpoint)

    def officers(self, company_number):
        """Get a list of officers for a company"""
        endpoint = "/company/{company_number}/officers".replace(
            "{company_number}", company_number
        )

        return self._http_get_request(endpoint)

    def search_company(self, query):
        """Search for a company"""
        endpoint = "/search/companies?q={query}".replace("{query}", query)

        return self._http_get_request(endpoint)

    def corporate_entity_beneficial_owner(self, psc_id):
        """Get a corporate entity beneficial owner"""
        endpoint = str.join(
            "/company/{company_number}/",
            "persons-with-significant-control/corporate-entity-beneficial-owner/{psc_id}",
        ).replace("{psc_id}", psc_id)

        return self._http_get_request(endpoint)

    def corporate_entities(self, psc_id):
        """Get a corporate entity"""
        endpoint = str.join(
            "/company/{company_number}/",
            "persons-with-significant-control/corporate-entity/{psc_id}",
        ).replace("{psc_id}", psc_id)

        return self._http_get_request(endpoint)

    def individual_beneficial_owner(self, psc_id):
        """Get an individual beneficial owner"""
        endpoint = str.join(
            "/company/{company_number}/",
            "persons-with-significant-control/individual-beneficial-owner/{psc_id}",
        ).replace("{psc_id}", psc_id)

        return self._http_get_request(endpoint)

    def get_individual(self, psc_id):
        """Get an individual"""
        endpoint = str.join(
            "/company/{company_number}",
            "/persons-with-significant-control/individual/{psc_id}",
        ).replace("{psc_id}", psc_id)

        return self._http_get_request(endpoint)

    def legal_person_beneficial_owner(self, psc_id):
        """Get a legal person beneficial owner"""
        endpoint = str.join(
            "/company/{company_number}",
            "/persons-with-significant-control/legal-person-beneficial-owner/{psc_id}",
        ).replace("{psc_id}", psc_id)

        return self._http_get_request(endpoint)

    def legal_persons(self, psc_id):
        """Get a legal person"""
        endpoint = str.join(
            "/company/{company_number}",
            "/persons-with-significant-control/legal-person/{psc_id}",
        ).replace("{psc_id}", psc_id)

        return self._http_get_request(endpoint)

    def statement(self, statement_id):
        """Get a statement"""
        endpoint = str.join(
            "/company/{company_number}",
            "/persons-with-significant-control-statements/{statement_id}",
        ).replace("{statement_id}", statement_id)

        return self._http_get_request(endpoint)

    def super_secure_beneficial_owner(self, super_secure_id):
        """Get a super secure beneficial owner"""
        endpoint = str.join(
            "/company/{company_number}/",
            "persons-with-significant-control/super-secure/{super_secure_id}",
        ).replace("{super_secure_id}", super_secure_id)

        return self._http_get_request(endpoint)

    def persons_with_significant_control_list(self, company_number):
        """Get a list of persons with significant control"""
        endpoint = "/company/{company_number}/persons-with-significant-control".replace(
            "{company_number}", company_number
        )

        return self._http_get_request(endpoint)

    def persons_with_significant_control_list_statements(self, company_number):
        """Get a list of persons with significant control statements"""
        endpoint = "/company/{company_number}/persons-with-significant-control-statements".replace(
            "{company_number}", company_number
        )

        return self._http_get_request(endpoint)
