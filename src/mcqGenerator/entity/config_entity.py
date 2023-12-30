from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from mcqGenerator.constants import *
TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME

    artifact_dir: str = Path(ARTIFACT_DIR, TIMESTAMP)

    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class McqGeneratorConfig:

    mcq_generator_dir: str = Path(
        training_pipeline_config.artifact_dir, MCQ_GENERATOR_DIR
    )

    
