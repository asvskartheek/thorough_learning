# looking at the pdf file there are:
# - 24 worked out examples
# - (6+5+11+9+11)=42 exercises
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

data_path = "data/extracted_jsons/math_11_ch6_pnc_att3.json"
with open(data_path, "r") as f:
    data = json.load(f)
    logger.info(f"Expected 24 examples, got {len(data['example_problems'])}")
    logger.info(f"Expected 42 exercises, got {len(data['exercises'])}")
