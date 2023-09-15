class Pagination:
    def __init__(self, data: str, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page

    @property
    def item_count(self):
        return len(self.data)

    @property
    def page_cut(self):
        tuple_page = tuple(self.data[i:i+self.items_on_page] for i in range(0, len(self.data), self.items_on_page))
        return tuple_page

    @property
    def page_count(self):
        return len(self.page_cut)

    def count_items_on_page(self, page_number: int):
        if (type(page_number) is not int) or (page_number > len(self.page_cut) - 1):
            raise Exception('Invalid index. Page is missing')
        return len(self.page_cut[page_number])

    def find_page(self, data2find: str):
        if (type(data2find) is str) and (data2find in self.data):
            start = -1
            index = []
            while self.data[start + 1:].find(data2find) != -1:
                start += self.data[start + 1:].find(data2find) + 1
                start_page = start // self.items_on_page
                end = start + len(data2find) - 1
                end_page = end // self.items_on_page
                for i in range(start_page, end_page + 1):
                    index.append(i)
            return index
        else:
            raise Exception(f'{data2find} is missing on the pages')

    def display_page(self, page_number: int):
        if (type(page_number) is not int) or (page_number > len(self.page_cut) - 1):
            raise Exception('Invalid index. Page is missing')
        return self.page_cut[page_number]
