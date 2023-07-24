
class DataSerialization(object):

    def __init__(self):
        self.data = ''
    @classmethod
    def sorted_data(cls, serializer_class):
        product_list = {'response_code': 200, 'message': "Success", 'data': []}
        for i_data in serializer_class.data:
            product_list['data'].append(dict(i_data))
        return product_list