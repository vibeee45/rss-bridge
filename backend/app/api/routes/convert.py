from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request

from app.models.convert_request import ConvertRequest
from app.services.convert_service import ConvertService

from app.exceptions.feed_exceptions import (
    FeedFetchError,
    InvalidFeedError
)

from app.exceptions.parser_exceptions import (
    UnsupportedFeedType
)

from app.exceptions.generator_exceptions import (
    GeneratorError
)

router = APIRouter()

convert_service = ConvertService()


@router.post("/")
def convert(
    payload: ConvertRequest,
    request: Request
):

    try:

        return convert_service.convert(
            url=str(payload.url),
            request=request
        )

    except FeedFetchError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    except InvalidFeedError as exc:

        raise HTTPException(
            status_code=422,
            detail=str(exc)
        )

    except UnsupportedFeedType as exc:

        raise HTTPException(
            status_code=415,
            detail=str(exc)
        )

    except GeneratorError as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )