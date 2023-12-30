from dataclasses import dataclass

@dataclass
class QuizArtifact:
    text: str
    number: int
    subject: str
    tone: str
    response_json: str
