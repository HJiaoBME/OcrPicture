#
import os
import json
import re
import base64
import numpy as np
import pandas as pd

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

path = 'p1.jpg'


def imgget(path):
    with open(path, 'rb') as f:
        img_data = f.read()
        img_base64 = base64.b64encode(img_data)
    return img_base64.decode('utf-8')
params = imgget(path)
print(params)

#
#
#
# import os
#
#
#
# from tencentcloud.common import credential
#
# from tencentcloud.common.profile.client_profile import ClientProfile
#
# from tencentcloud.common.profile.http_profile import HttpProfile
#
# from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
#
# from tencentcloud.ocr.v20181119 import ocr_client, models
#
# secret_id = 'AKIDOdgU1HH4dxFON6ntyqTyKakkY7QUavJX'
# secret_key = 'RuBJHZbRebgcDcqqjy62AOSOgw52qU9b'
#
# cred = credential.Credential(secret_id, secret_key)
#
# httpProfile = HttpProfile()
#
# httpProfile.endpoint = "ocr.tencentcloudapi.com"
#
#
#
# clientProfile = ClientProfile()
#
# clientProfile.httpProfile = httpProfile
#
# client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)
#
#
#
# req = models.GeneralFastOCRRequest()
#
# req.ImageUrl = "https://github.com/HJiaoBME/OcrPicture/blob/master/37463034464644302D363531342D344336432D413636432D344344424236444142394641.jpg"
#
# resp = client.GeneralFastOCR(req)
#
# print(resp.to_json_string())
#
#
#
