from fastapi import APIRouter
from schemas.emotions import EmotionsInput, EmotionsOutput
from pipelines.emotions import detect_emotions

router = APIRouter(
    prefix="/emotions",
    tags=["Emotions"],
    responses={404: {"description": "Not found"}},
)

@router.post('/', summary='Detect Emotions', response_model=EmotionsOutput)
def post_emotions(schema: EmotionsInput) -> EmotionsOutput:
    """
    Определить эмоции англоязычного текста. Первый запуск может занять некоторое время.
    """
    emotions_result = detect_emotions(schema)
    return {"text": schema.text, "emotions": emotions_result}