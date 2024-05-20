from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2

router = APIRouter(prefix="/vote", tags=["vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: schemas.Vote,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    print(current_user.id)
    vote_query = db.query(models.Vote).filter(
        
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            print(found_vote)
            raise HTTPException(status_code = status.HTTP_409_CONFLICT,detail='already voted')
        new_vote = models.Vote(post_id = vote.post_id,user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return 'voted succesfully'
    else:
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail='vote doesnt exist')
        vote_query.delete(synchronize_session=False)
        db.commit()
        return 'unvoted succesfully'
