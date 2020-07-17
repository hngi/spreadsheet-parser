import os
import json
import pandas as pd
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework_jwt.settings import api_settings

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


