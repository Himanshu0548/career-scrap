from scrappers import COMPANY_LOGO_MAP


class PostingRepository:
    size = 0

    def __init__(self, db):
        self.postings = {}
        self.db = db

    def update_postings(self, company, postings):
        self.db.remove_by_company(company)
        for posting in postings:
            self.db.insert(posting['title'], posting['location'], posting['url'], company)

    def get_postings(self):
        data = self.db.get_all()
        for posting in data:
            posting['logo'] = COMPANY_LOGO_MAP[posting['company']]
        return data

    def search_postings(self, text):
        data = self.db.search(text)
        for posting in data:
            posting['logo'] = COMPANY_LOGO_MAP[posting['company']]
        return data

    def get_companies(self):
        return self.db.get_company_list()

    def get_size(self):
        return self.db.get_count()
