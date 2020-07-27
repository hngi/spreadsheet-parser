import os
import json
import pandas as pd
from dotenv import load_dotenv
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.generics import ListAPIView
from .permissions import IsOwnerOrReadOnly
from rest_framework_jwt.settings import api_settings
import datetime
import ssl
from json import JSONEncoder
from benedict import benedict

ssl._create_default_https_context = ssl._create_unverified_context
# Create your views here.


payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

load_dotenv()
class ProductPagination(PageNumberPagination):
    page_size = 20

class ExcelintroAPIView(ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = PostLimitOffsetPagination
    

    def post(self, request):
        pagination_class = PostLimitOffsetPagination
        # print('.>>>>>', request.GET.get('q', None))
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')
        if api_key == user_api_key:
            file_path = request.data.get('file_path')
            column = request.data.get('column')
            if file_path and column:
                df = pd.read_excel(file_path, encoding='utf-8', )
                data = df.dropna(axis=0, how='any')
                loc = data.loc[column-1:]
                final_data = loc.to_dict(orient='records')

                return Response(json.loads(json.dumps(final_data)), status=status.HTTP_200_OK)
            if file_path:
                df = pd.read_excel(file_path, encoding='utf-8', )
                data = df.dropna(axis=0, how='any')
                data.columns = data.columns.map(lambda x: str(x))
                data.columns = data.columns.map(lambda x: x.replace('\n', ''))
                final_data = data.to_dict(orient='records')
                test = benedict(final_data)
                print(test)

                return Response(json.loads(json.dumps(final_data)), status=status.HTTP_200_OK)
                
            else:
                return Response({'error': 'file path can not be empty'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)

# {"file_path":"https://file-examples-com.github.io/uploads/2017/02/file_example_XLSX_10.xlsx","API_KEY":"whatiftheworldendstodayum"}
# {"file_path":"https://file-examples-com.github.io/uploads/2017/02/file_example_XLSX_10.xlsx","from":2,"to":7,"API_KEY":"whatiftheworldendstodayum"}

class ExcelAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = PostLimitOffsetPagination
    def post(self, request):
        if request.method == 'POST':
            api_key = os.getenv('API_KEY')
            user_api_key = request.data.get('API_KEY')
            if api_key == user_api_key:
                file_path = request.data.get('file_path')
                row_from = request.data.get('row_from')
                row_to = request.data.get('row_to')
                col_from = request.data.get('col_from')
                col_to = request.data.get('col_to')
                sheet = request.data.get("sheet")
                try:
                    if file_path and row_from and row_to:
                        data = pd.read_excel(file_path, sheet_name=sheet)
                        if type(data) is dict:
                            ano = pd.concat(((data[frame]) for frame in data.keys()),ignore_index=True)
                            data1 = ano.dropna(axis=0, how='all', thresh=3)
                            data2 = data1.dropna(axis=1, how='all')
                            new = data2.loc[data2.isnull().mean(axis=1).lt(0.3)]
                            new2 = new[new.columns[new.isnull().mean()<0.3]]

                            if 'Unnamed: 2' in new2.columns:
                                new_header = new2.iloc[0]
                                new2.columns = new_header
                                if "-" in new2.columns:
                                    new_header = new2.iloc[1]
                                    new2.columns = new_header
                                new2 = new2[1:]
                            new2 = new2.fillna('').reset_index(drop = True)
                            new3 = new2.loc[row_from:row_to]
                            new3 = new3.iloc[:,col_from:col_to]
                            
                            daily_expenses = new3.to_dict(orient='records')
                            class DateTimeEncoder(JSONEncoder):
                                def default(self, obj):
                                    if isinstance(obj, (datetime.date, datetime.datetime)):
                                        return obj.isoformat()
                            ohh = json.dumps(daily_expenses,cls=DateTimeEncoder)
                            
                            real_data = json.loads(ohh)
                            return Response(real_data, status= status.HTTP_200_OK)
                        data1 = data.dropna(axis=0, how='all', thresh=3)
                        data2 = data1.dropna(axis=1, how='all')
                        new = data2.loc[data.isnull().mean(axis=1).lt(0.3)]
                        new2 = new[new.columns[new.isnull().mean()<0.3]]

                        if 'Unnamed: 2' in new2.columns:
                            new_header = new2.iloc[0]
                            new2.columns = new_header
                            if "-" in new2.columns:
                                new_header = new2.iloc[1]
                                new2.columns = new_header
                            new2 = new2[1:]
                        new2 = new2.fillna('').reset_index(drop = True)
                        new3 = new2.loc[row_from:row_to]
                        new3 = new3.iloc[:,col_from:col_to]
                        
                        daily_expenses = new3.to_dict(orient='records')
                        class DateTimeEncoder(JSONEncoder):
                                def default(self, obj):
                                    if isinstance(obj, (datetime.date, datetime.datetime)):
                                        return obj.isoformat()
                        ohh = json.dumps(daily_expenses,cls=DateTimeEncoder)
                       
                        real_data = json.loads(ohh)
                        return Response(real_data, status= status.HTTP_200_OK)

                    elif file_path and row_from:
                        data = pd.read_excel(file_path, sheet_name=sheet)
                        if type(data) is dict:
                            ano = pd.concat(((data[frame]) for frame in data.keys()),ignore_index=True)
                            data1 = ano.dropna(axis=0, how='all', thresh=3)
                            data2 = data1.dropna(axis=1, how='all')
                            new = data2.loc[data2.isnull().mean(axis=1).lt(0.3)]
                            new2 = new[new.columns[new.isnull().mean()<0.3]]

                            if 'Unnamed: 2' in new2.columns:
                                new_header = new2.iloc[0]
                                new2.columns = new_header
                                if "-" in new2.columns:
                                    new_header = new2.iloc[1]
                                    new2.columns = new_header
                                new2 = new2[1:]
                            new2 = new2.fillna('').reset_index(drop = True)
                            new3 = new2.loc[row_from:row_to]
                            new3 = new3.iloc[:,col_from:col_to]
                            
                            daily_expenses = new3.to_dict(orient='records')
                            print(daily_expenses)
                            class DateTimeEncoder(JSONEncoder):
                                def default(self, obj):
                                    if isinstance(obj, (datetime.date, datetime.datetime)):
                                        return obj.isoformat()
                            ohh = json.dumps(daily_expenses,cls=DateTimeEncoder)
                            real_data = json.loads(ohh)
                            return Response(real_data, status= status.HTTP_200_OK)
                    
                        data1 = data.dropna(axis=0, how='all', thresh=3)
                        
                        data2 = data1.dropna(axis=1, how='all')                 
                        new = data2.loc[data.isnull().mean(axis=1).lt(0.3)]
                        new2 = new[new.columns[new.isnull().mean()<0.3]]

                        if 'Unnamed: 2' in new2.columns:
                            new_header = new2.iloc[0]
                            new2.columns = new_header
                            if "-" in new2.columns:
                                new_header = new2.iloc[1]
                                new2.columns = new_header                           
                            new2 = new2[1:]
                        new2 = new2.fillna('').reset_index(drop = True)
                        new3 = new2.loc[row_from:]
                        new3 = new3.iloc[:,col_from:col_to]
                        
                        daily_expenses = new3.to_dict(orient='records')
                        class DateTimeEncoder(JSONEncoder):
                                def default(self, obj):
                                    if isinstance(obj, (datetime.date, datetime.datetime)):
                                        return obj.isoformat()
                        ohh = json.dumps(daily_expenses,cls=DateTimeEncoder)
                        
                        real_data2 = json.loads(ohh)
                        return Response(real_data2, status= status.HTTP_200_OK)
                    elif file_path:
                        data = pd.read_excel(file_path,sheet_name=sheet)
                        if type(data) is dict:
                            ano = pd.concat(((data[frame]) for frame in data.keys()),ignore_index=True)
                            data1 = ano.dropna(axis=0, how='all', thresh=3)
                            data2 = data1.dropna(axis=1, how='all')
                            new = data2.loc[data2.isnull().mean(axis=1).lt(0.3)]
                            new2 = new[new.columns[new.isnull().mean()<0.3]]

                            if 'Unnamed: 2' in new2.columns:
                                new_header = new2.iloc[0]
                                new2.columns = new_header
                                if "-" in new2.columns:
                                    new_header = new2.iloc[1]
                                    new2.columns = new_header
                                new2 = new2[1:]
                            new2 = new2.fillna('').reset_index(drop = True)
                            new3 = new2.loc[row_from:row_to]
                            new3 = new3.iloc[:,col_from:col_to]
                            
                            daily_expenses = new3.to_dict(orient='records')
                            
                            class DateTimeEncoder(JSONEncoder):
                                def default(self, obj):
                                    if isinstance(obj, (datetime.date, datetime.datetime)):
                                        return obj.isoformat()
                            ohh = json.dumps(daily_expenses,cls=DateTimeEncoder)
                            real_data = json.loads(ohh)
                            return Response(real_data, status= status.HTTP_200_OK)
                    
                        data1 = data.dropna(axis=0, how='all', thresh=3)
                        data2 = data1.dropna(axis=1, how='all')
                                            
                        new = data2.loc[data.isnull().mean(axis=1).lt(0.3)]
                        new2 = new[new.columns[new.isnull().mean()<0.3]]
                        if 'Unnamed: 2' in new2.columns:
                            new_header = new2.iloc[0]
                            new2.columns = new_header
                            if "-" in new2.columns:
                                new_header = new2.iloc[1]
                                new2.columns = new_header
                            
                            new2 = new2[1:]
                        new2 = new2.fillna('').reset_index(drop = True)
                        new2 = new2.iloc[:,col_from:col_to]
                        daily_expenses = new2.to_dict(orient='records')
                        class DateTimeEncoder(JSONEncoder):
                                def default(self, obj):
                                    if isinstance(obj, (datetime.date, datetime.datetime)):
                                        return obj.isoformat()
                        ohh = json.dumps(daily_expenses,cls=DateTimeEncoder)
                        real_data2 = json.loads(ohh)
                        return Response(real_data2, status= status.HTTP_200_OK)

                except IndexError:
                    return Response({'error':'Your excel link doesnt have the sheet specified.(sheet start from zero)'}, status = status.HTTP_404_NOT_FOUND)

                else:
                    return Response({'error': 'file path can not be empty'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'you are not authorized to perform this action.'},
                                status=status.HTTP_401_UNAUTHORIZED)
#{"file_path":"https://fgn-web-crawler.herokuapp.com/static/expense/2020/01_02_2020.xlsx","row_from":20,"row_to":50,"col_from":0,"col_to":3,"API_KEY":"random25stringsisneeded"}

#{"file_path":"https://fgn-web-crawler.herokuapp.com/static/expense/2020/01_02_2020.xlsx","API_KEY":"whatiftheworldendstodayum"}
#{"file_path":"https://opentreasury.gov.ng/images/2020/DAILYPAYMENT/JULY/04-07-20.xlsx","API_KEY":"whatiftheworldendstodayum"}
# {"file_path":"https://opentreasury.gov.ng/images/2020/DAILYPAYMENT/MARCH/11-03-20.xlsx","API_KEY":"random25stringsisneeded"}
# {"file_path":"https://opentreasury.gov.ng/images/2020/MONTHLYBUDPERF/FGN/ADMIN/FEB.xlsx","API_KEY":"whatiftheworldendstodayum"}
# {"file_path":"https://fgn-web-crawler.herokuapp.com/static/expense/2020/01_02_2020.xlsx","row_from":20,"row_to":22,"col_from":2,"col_to":4,"API_KEY":"whatiftheworldendstodayum"}
#{"file_path":"https://drive.google.com/u/0/uc?id=1NSXTR1jaP_YUkpqeatMdyjHWwixoq2YP&export=download","API_KEY":"whatiftheworldendstodayum"}
# {"file_path":"https://drive.google.com/u/0/uc?id=1NSXTR1jaP_YUkpqeatMdyjHWwixoq2YP&export=download","row_from":3,"row_to":6,"col_from":4,"col_to":5,"sheet":1,"API_KEY":"whatiftheworldendstodayum"}
# {"file_path":"https://drive.google.com/u/0/uc?id=1NSXTR1jaP_YUkpqeatMdyjHWwixoq2YP&export=download","row_from":3,"row_to":6,"col_from":4,"col_to":5,"API_KEY":"whatiftheworldendstodayum"}
# {"file_path":"https://drive.google.com/u/0/uc?id=1NSXTR1jaP_YUkpqeatMdyjHWwixoq2YP&export=download","sheet":[0,1],"API_KEY":"whatiftheworldendstodayum"}