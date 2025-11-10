from langchain_core.tools import tool
from typing import Annotated, List
import logging

logger = logging.getLogger(__name__)    

@tool
def system_knowledge(
    query: Annotated[str, "To retrieve the system knowledge of KYC"],
) -> str:
    """
    Get system knowledge like:
    1. system architecture
    2. system description
    3. system dependencies
    4. system database information
    """


    logger.debug(f"Retrieving system knowledge for : {query}")
    
    rsp = '''The KYC comprises a sophisticated architecture of interconnected subsystems, each serving distinct compliance functions.
    
    1.The subsystem includes:
    子系统名|||描述
    IDAP-ACSC|||KYC访问控制服务核心子系统，负责外部客户调用SAAS服务时，提供安全且精细的访问控制策略，提高系统的可扩展性和灵活性，以满足不断变化的业务需求。
    IDAP-ADMIN|||"用于查询人脸验证明细，统计报表，服务注册等工作管理平台。
    提供给合作伙伴和运营人员使用"
    IDAP-AIALD|||AI视频动作活体检测服务，通过接受采集的视频信息，检测视频中的人是否为真实活体。
    IDAP-AIARLD|||AI动作加反光检测服务，通过接收移动端采集的人脸光线变化差异图成像+人脸动作视频，模型结合各类活体检测服务，验证是否真人
    IDAP-AICF|||AI图片切脸服务，通过接受采集的图像，识别图片最大人脸位置进行抠图，得到仅含目标人脸的图片。
    IDAP-AIFAD|||AI人脸属性检测服务，通过接受采集的图像信息，检测图片人脸的性别和年龄、面膜和帽子等属性。
    IDAP-AIFC|||AI人像比对服务，用于比对用户扫脸与证件/高清照片的结果。验证结果包含人脸比对得分
    IDAP-AIFCG|||针对特定用户，通过接受客户上传的人脸视频里采集的人脸图像信息，结合客户上送的人像比对图片，本模型检测两张图片的人像相似度，确认是否为同一人
    IDAP-AIFFC|||针对特定用户，通过接受客户上传的人脸视频或照片里采集的人脸的512个维度特征信息，结合客户上送的人像特征比对信息，本模型检测两组特征信息的相似度，确认是否为同一人
    IDAP-AIFQD|||AI人脸质量检测服务，通过接受采集的图像信息，检测图片人脸的遮挡、闭眼和清晰度等属性。
    IDAP-AIHLD|||AIH5活体检测服务，针对特定用户，通过接受采集的影像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-AIHRLD|||AIH5一闪活体检测服务，针对特定用户，通过接受采集的影像信息和反光信息，模型结合各类活体检测服务，验证是否真人
    IDAP-AIICU|||AI图片内容理解服务，通过接受采集的图像，检测图像是否存在用户需要进行识别的标签信息，如佩戴墨镜、佩戴口罩等
    IDAP-AIOCR|||由AI提供的OCR模型，提供OCR文字识别服务，通过接受上游业务核心系统采集的图像信息，识别图片中文字内容信息并返回。
    IDAP-AIPLD|||AI图片活体检测服务，通过接受采集的图像，识别图片中的人是否为真实活体。
    IDAP-AIPLE|||AI图片活体检测增强服务，针对特定客户，通过接受采集的图像，识别图片中的人是否为真实活体
    IDAP-AISILD|||AI选图和唇语检测服务，通过接受采集的视频，选取多张最优帧图片以及检测视频中的人嘴唇是否有动作
    IDAP-ARNG|||nginx负载均衡服务，用于将H5实时人像识别场景下，一闪光线识别模式中，人脸识别流程里的同一流程数据流传送到同一台模型服务器中。
    IDAP-BDP|||负责云上大数据分析和后台核心的交互
    IDAP-CIDAAC|||行内与云身份验证服务对接的前置，提供银行AI大模型识别用户意图服务，KYC账单计提汇总服务，KYC WA数据分析服务。
    IDAP-DRAC|||KYC独立意愿表达服务前置子系统，通过接入腾讯云TRTC(Tencent Real-Time Communication)服务，接收实时输入的音视频并处理。
    IDAP-DRSC|||KYC独立意愿表达服务核心子系统，通过接收用户的意愿性音视频，做意愿性识别等处理。
    IDAP-DRWEB|||该子系统用于KYC独立意愿表达服务浏览器前端静态资源访问
    IDAP-GEWEB|||用于APP Webview、各大手机浏览器，提供云刷脸SaaS服务
    IDAP-IDASC|||身份验证服务核心，负责身份验证服务的整体业务逻辑主控，标准化身份验证结果并返回给前端。
    IDAP-IDCORE|||身份照片信息服务核心，负责对身份照片信息的存储和管理
    IDAP-IDIAC|||身份照片信息服务前置，与第三方身份返照服务商对接，负责调用第三方服务，获取返回的照片信息和存储。
    IDAP-NG|||提供定制化的HTTP服务请求路由能力，将语音、视频等数据流路由到语音识别、图像识别等AI算法处理系统，确保同一数据包的所有分片落在同一个数据处理服务器上
    IDAP-OPENAPI|||OPENAPI前置服务器，提供SaaS服务的接入鉴权，为第三方业务（App）、H5提供Oauth2认证、鉴权和资源访问服务, 同时提供接入之前的相关接口服务。
    IDAP-OPENAPIPS|||OPENAPI前置服务器,提供PaaS服务的接入鉴权。
    IDAP-REPORT|||KYC数据服务子系统定位于实现 KYC 业务需要的各类数据加工，数据报表，账单等数据服务。
    IDAP-RMDT|||视频帧或视频合并转码服务。支持纯H5实时刷脸场景下，在人脸识别模型处理之前，合并和转换处理不同视频帧数据，实现图片与视频间的转换。用于后续的人像识别
    IDAP-TRTCAC|||KYC TRTC 服务前置子系统,访问腾讯云TRTC服务
    IDAP-VDT|||支持纯H5刷脸时，不同C端机型摄像头录制的视频大小不一样，在人脸识别模型处理之前，需要进行压缩和转换处理。
    IDAP-WSAC|||提供通过webSocket访问系统，支持纯H5实时刷脸时的帧数据处理与转发能力。
    IDAP-YTAARD|||一闪活体服务，通过接收移动端采集的人脸光线变化差异图成像+人脸动作视频，根据风控等级选择模型类型并结合各类活体检测服务，验证是否真人
    IDAP-YTAARDG|||一闪动作加反光活体灰度服务，通过接收移动端采集的人脸光线变化差异图成像+人脸动作视频，验证是否真人
    IDAP-YTALD|||视频动作活体服务，通过接收移动端用户动作视频，模型结合各类活体检测服务，验证是否真人
    IDAP-YTALDG|||视频动作活体灰度模式服务，针对特定用户，通过接受采集的影像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTALDPC|||视频动作活体PC检测服务，通过接受采集的影像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTFAD|||优图人脸属性检测服务，通过接受采集的图像信息，检测图片人脸的性别和年龄等属性
    IDAP-YTFC|||用于比对用户扫脸与证件/高清照片的结果。验证结果包含人脸比对得分和活体检测
    IDAP-YTFCLD|||优图远近活体检测服务，通过接受采集的连续图片帧，检测帧序列的人脸是否为真人
    IDAP-YTFQD|||人脸质量检测服务，通过接受采集的图像信息，检测图像的人脸质量信息是否符合标准
    IDAP-YTHLD|||H5视频活体检测服务，针对特定用户，通过接受采集的影像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTHRLD|||H5一闪实时监测服务，针对特定用户，通过接受采集的影像信息和反光信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTLDN|||数字活体服务，通过接受采集的语音视频文件，模型结合各类活体检测服务，验证是否真人
    IDAP-YTLDNG|||数字活体灰度服务，针对特定用户，通过接受采集的语音视频文件，模型结合各类活体检测服务，验证是否真人
    IDAP-YTLLD|||光线活体服务，通过接收移动端采集的人脸光线变化差异图成像，模型结合各类活体检测服务，验证是否真人
    IDAP-YTOCRBC|||银行卡OCR识别服务，包含识别和防伪检测等，提取证件内的相关文字信息或图片信息。
    IDAP-YTOCRDL|||驾驶证/行驶证OCR识别服务，包含识别和防伪检测等，提取证件内的相关文字信息或图片信息。
    IDAP-YTOCRIDC|||身份证OCR识别服务，包含识别和防伪检测等，提取证件内的相关文字信息或图片信息。
    IDAP-YTOCRIDCPS|||优图OCR场景的身份证PS检测服务，通过接受采集的身份证图片，检测图片是否为人工PS图片
    IDAP-YTPLD|||图片活体检测服务，通过接受采集的图像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTPLDD|||图片活体检测出行模式服务，针对出行行业，通过接受采集的图像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTPLDPC|||图片活体检测PC模式服务，针对特定PC用户，通过接受采集的图像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTPLG|||图片活体检测灰度模式服务，针对特定用户，通过接受采集的图像信息，模型结合各类活体检测服务，验证是否真人
    IDAP-YTSILD|||优图选图和唇语检测服务，通过接受采集的视频，选取多张最优帧图片以及检测视频中的人嘴唇是否有动作
    IDAP-YTSLD|||静默活体检测服务，通过接受采集的影像信息，模型结合各类活体检测服务，验证是否真人

    2.The relationship among these subsystems is as follows:
    客户端 --> 公网 --> WBC-NGINX
    腾讯云 --> 专线 --> WBC-NGINX(域名idate.webank.com)
    WBC-NGINX --> IDAP-OPENAPI
    WBC-NGINX --> IDAP-OPENAPIPS
    WBC-NGINX --> IDAP-TRTCAC
    WBC-NGINX --> IDAP-WSAC
    WBC-NGINX --> WBC-PARTNER
    WBC-NGINX --> IDAP-DRAC
    IDAP-OPENAPI --> IDAP-IDASC
    IDAP-OPENAPI --> IDAP-ACSC
    IDAP-OPENAPI --> IDAP-VDT
    IDAP-OPENAPI --> WBC-AUTH
    IDAP-OPENAPI --> WBC-SC
    IDAP-OPENAPIPS --> IDAP-IDASC
    IDAP-OPENAPIPS --> WBC-AUTH
    IDAP-OPENAPIPS --> WBC-SC
    IDAP-WSAC --> IDAP-RMDT
    IDAP-WSAC --> WBC-SC
    IDAP-WSAC --> WBC-AUTH
    IDAP-WSAC --> IDAP-IDASC
    IDAP-WSAC --> IDAP-NG
    IDAP-WSAC --> IDAP-ARNG
    IDAP-TRTCAC --> IDAP-IDASC
    IDAP-TRTCAC --> IDAP-VDT
    IDAP-TRTCAC --> WBC-SC
    IDAP-TRTCAC --> WBC-AUTH
    IDAP-TRTCAC --> IDAP-NG
    IDAP-TRTCAC --> IDAP-ARNG
    IDAP-DRAC --> IDAP-DRSC
    IDAP-DRAC --> IDAP-VDT
    IDAP-DRAC --> WBC-AUTH
    IDAP-DRSC --> IDAP-VDT
    IDAP-DRSC --> WBC-FPS
    IDAP-DRSC --> IDAP-IDIAC
    IDAP-IDIAC --> IDAP-IDASC
    IDAP-IDASC --> IDAP-IDCORE
    IDAP-IDASC --> IDAP-IDIAC
    IDAP-IDASC --> IDAP-VDT
    IDAP-IDASC --> IDAP-ACSC
    IDAP-IDASC --> WBC-WBAC
    IDAP-IDASC --> WBC-FPS
    IDAP-IDASC --> WBC-FPSAC
    IDAP-IDASC --> IDAP-ADMIN
    IDAP-IDASC --> IDAP-AIALD
    IDAP-IDASC --> IDAP-AIARLD
    IDAP-IDASC --> IDAP-AICF
    IDAP-IDASC --> IDAP-AIFAD
    IDAP-IDASC --> IDAP-AIFC
    IDAP-IDASC --> IDAP-AIFCG
    IDAP-IDASC --> IDAP-AIFFC
    IDAP-IDASC --> IDAP-AIFQD
    IDAP-IDASC --> IDAP-AIHLD
    IDAP-IDASC --> IDAP-AIHRLD
    IDAP-IDASC --> IDAP-AIICU
    IDAP-IDASC --> IDAP-AIOCR
    IDAP-IDASC --> IDAP-AIPLD
    IDAP-IDASC --> IDAP-AIPLE
    IDAP-IDASC --> IDAP-AISILD
    IDAP-IDASC --> IDAP-YTAARD
    IDAP-IDASC --> IDAP-YTAARDG
    IDAP-IDASC --> IDAP-YTALD
    IDAP-IDASC --> IDAP-YTALDG
    IDAP-IDASC --> IDAP-YTALDPC
    IDAP-IDASC --> IDAP-YTFAD
    IDAP-IDASC --> IDAP-YTFC
    IDAP-IDASC --> IDAP-YTFCLD
    IDAP-IDASC --> IDAP-YTFQD
    IDAP-IDASC --> IDAP-YTHLD
    IDAP-IDASC --> IDAP-YTHRLD
    IDAP-IDASC --> IDAP-YTLDN
    IDAP-IDASC --> IDAP-YTLDNG
    IDAP-IDASC --> IDAP-YTLLD
    IDAP-IDASC --> IDAP-YTOCRBC
    IDAP-IDASC --> IDAP-YTOCRDL
    IDAP-IDASC --> IDAP-YTOCRIDC
    IDAP-IDASC --> IDAP-YTOCRIDCPS
    IDAP-IDASC --> IDAP-YTPLD
    IDAP-IDASC --> IDAP-YTPLDD
    IDAP-IDASC --> IDAP-YTPLDPC
    IDAP-IDASC --> IDAP-YTPLG
    IDAP-IDASC --> IDAP-YTSILD
    IDAP-IDASC --> IDAP-YTSLD
    IDAP-ARNG --> IDAP-YTHRLD
    IDAP-NG --> IDAP-YTHLD
    IDAP-IDIAC --> 云生产ECN代理 --> 行内ECN代理 --> welb-nonginx --> IDAP-CIDAAC --> 大模型
    IDAP-IDIAC --> 第三方渠道

    第三方渠道包含
    交科信用-二要素
    华付-二要素
    海鑫-二要素
    骏聿-二要素
    云盾-二要素
    证通-二要素
    金保信-二要素
    金保信-人像比对
    证通-人像比对
    骏聿-人像比对
    云盾-人像比对
    海鑫新一所-人像比对
    交科信用_新一所-人像比对
    华付一所二渠道-人像比对
    华付一所一渠道 - 人像比对
    腾讯云ASR识别
    腾讯云TTS转语音
    腾讯内容审核
    腾讯背景模板检索
    腾讯AI防护盾
    AI大模型
    图灵盾
    相机图灵盾
    3. Database Information:
    subsystem|||database_name|||description|||db_type
    idap-idasc|||idap_idasc|||身份验证服务核心数据库|||MySQL
    '''

    return rsp