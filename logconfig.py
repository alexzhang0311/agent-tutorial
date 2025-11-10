import logging
import logging.config
from pathlib import Path

def setup_logging():
    """配置项目全局日志"""
    log_dir = Path(__file__).parent/ "logs"
    print(f"日志目录: {log_dir}")
    log_dir.mkdir(exist_ok=True)
    
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(threadName)s - %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'standard',
                'filename': log_dir / 'agent.log',
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5,
                'encoding': 'utf8'
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            },
            'src': {
                'handlers': ['console','file'],
                'level': 'DEBUG',
                'propagate': False
            },
        }
    }
    
    logging.config.dictConfig(log_config)

# 初始化日志
setup_logging()

# 导出logger供其他模块使用
logger = logging.getLogger(__name__)