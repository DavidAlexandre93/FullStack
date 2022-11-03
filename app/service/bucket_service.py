import boto3
import csv, sys
from fastapi import HTTPException, Depends
from starlette.responses import JSONResponse, Response
from app.database.connection import AsyncSession, get_session
from app.database.models import CessaoFundo
# from app.model.bucket_request import EmailRequest
# from app.model.bucket_response import EmailResponse


class BucketS3:

    @staticmethod
    def readFileBucketLambda(event, context) -> JSONResponse:

        # TODO VARS
        nome_do_arquivo_download = "arquivo_exemplo.csv"
        nome_do_s3 = "nome_do_bucket_s3"

        # TODO Download e Leitura do Bucket S3
        s3 = boto3.resource('s3')
        obj = s3.Object(nome_do_s3, nome_do_arquivo_download)
        body = obj.get()['Body'].read().decode()

        return JSONResponse(status_code=200, content=body)

    @staticmethod
    async def fileReadBucket():

        arquivo = 'arquivo_exemplo.csv'
        with open(arquivo, 'rb') as arq:
            reader = csv.reader(arq, delimiter=';', quoting=csv.QUOTE_NONE)
            try:
                for linha in reader:
                    print
                    linha
            except csv.Error as e:
                sys.exit('arquivo %s, linha %d: %s' % (arquivo, reader.line_num, e))

        return reader

    @staticmethod
    async def fileSaveData(db: AsyncSession = Depends(get_session)) -> Response:

        async with db as session:
            query = CessaoFundo('%s', '%s', '%s')
            try:
                session.add(query)
                await session.commit()
            except Exception as error:
                raise HTTPException(404, detail=str(error))

        return Response(status_code=200, content={"message": "Email enviado com sucesso!"})
