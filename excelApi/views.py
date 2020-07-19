import os
import json
import pandas as pd
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework_jwt.settings import api_settings
from datetime import datetime

# Create your views here.


payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

load_dotenv()


class ExcelAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request):
        # print('.>>>>>', request.GET.get('q', None))
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')
        if api_key == user_api_key:
            file_path = request.data.get('file_path')
            if file_path:
                df = pd.read_excel(file_path, encoding='utf-8')
                data = df.dropna(axis=0, how='any')
                data.columns = data.columns.map(lambda x: str(x))
                data.columns = data.columns.map(lambda x: x.replace('\n', ''))
                final_data = data.to_dict(orient='records')

                return Response(json.loads(json.dumps(final_data)), status=status.HTTP_200_OK)
            else:
                return Response({'error': 'file path can not be empty'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)


class dailyAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    
    def post(self, request):
        if request.method == 'POST':

            api_key = os.getenv('API_KEY')
            user_api_key = request.data.get('API_KEY')
            if api_key == user_api_key:
                file_path = request.data.get('file_path')
                if file_path:
                    data = pd.read_excel(file_path, sheet_name=0, usecols='C:F')
                    data1 = data.dropna(axis=0, how='all', thresh=3)
                    data2 = data1.dropna(axis=1, how='all')
                    
                    data2.columns = data2.iloc[0]
                    #if 'Description' in data2.columns:
                    #data2 = data2.iloc[1:, ].reindex()

                    # else:
                    data2.columns = data2.iloc[1]
                    data2 = data2.iloc[2:, ].reindex()

                    #     data2.columns = data2.columns.str.lower()
                    # df = data2.rename(columns={'beneficiary name': 'project_recipient_name', 'amount': 'project_amount',
                    # 'description': 'project_description', 'organization name': 'organization_name'})
                    # df['project_amount'] = df['project_amount'].apply(lambda x: '{:.2f}'.format(x))

                            # store data in dict form. this is the data to loop over to store into db
                    #date = datetime.strptime(name, '%d-%m-%Y').date()
                    data2 = data2.fillna('')
                    daily_expenses = data2.to_dict(orient='records')
                    
                    ohh = json.dumps(daily_expenses)
                    print(ohh)
                    real_data = json.loads(ohh)
                    print(ahh)
                    return Response(real_data, status= status.HTTP_200_OK)
                else:
                    return Response({'error': 'file path can not be empty'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'you are not authorized to perform this action.'},
                                status=status.HTTP_401_UNAUTHORIZED)
