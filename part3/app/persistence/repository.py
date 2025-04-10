from abc import ABC, abstractmethod
from app import db
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value, all=False):
        pass


class SQLAlchemyRepository(Repository):
    def __init__(self, model):  
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value, all=False):
        
        query = self.model.query.filter_by(**{attr_name: attr_value})
        if all:
            return query.all()
        return query.first()


class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self): 
        super().__init__(Place)

    def add(self, place, amenities):
        db.session.add(place)

        if amenities:
            amenities_ids = [Amenity.query.filter_by(id=amenity_id).first() for amenity_id in amenities]
            place.place_amenities.extend(amenities_ids)

        db.session.flush()
        db.session.commit()
        return place

    def update(self, place_id, place_data, amenities):
        place = self.get(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)

            if amenities:
                place.place_amenities = [Amenity.query.filter_by(id=amenity_id).first() for amenity_id in amenities]
            
            db.session.flush()
            db.session.commit()
            return place
        return None

    def delete(self, place_id):
        place = self.get(place_id)
        if place:
            Review.query.filter(Review.place_id == place_id).delete(synchronize_session=False)
            db.session.delete(place)
            db.session.commit()

    def get_place(self, place_id, options=None):
        query = Place.query.filter_by(id=place_id)
        if options:
            query = query.options(*options)
        return query.first()


class AmenitiesRepository(SQLAlchemyRepository):
    def __init__(self):  
        super().__init__(Amenity)


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_review_by_place(self, place_id):
        return self.model.query.filter_by(place_id=place_id).all()
