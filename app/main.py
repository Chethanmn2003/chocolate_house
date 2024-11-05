from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .models import SeasonalFlavor, Ingredient, CustomerFeedback
from .database import SessionLocal, init_db

# Initialising the database
init_db()
db = SessionLocal()

def add_seasonal_flavor(name: str, price: float):
    try:
        flavor = SeasonalFlavor(name=name, price=price)
        db.add(flavor)
        db.commit()
        db.refresh(flavor)
        return flavor
    except Exception as e:
        print(f"Error adding seasonal flavor: {e}")
        return None




def add_ingredient(name: str, quantity: int):
    # Check if ingredient already exists or not
    existing_ingredient = db.query(Ingredient).filter_by(name=name).first()

    if existing_ingredient:
        print(f"Ingredient '{name}' already exists. Updating quantity.")
        existing_ingredient.quantity += quantity  # Update if it already exists
        db.commit()
        db.refresh(existing_ingredient)
        return existing_ingredient
    else:
        # Add a new ingredient
        ingredient = Ingredient(name=name, quantity=quantity)
        db.add(ingredient)
        try:
            db.commit()
            db.refresh(ingredient)
            print(f"Ingredient '{name}' added successfully.")
            return ingredient
        except IntegrityError:
            db.rollback()
            print(f"Failed to add ingredient '{name}' due to a database error.")
            return None

def add_customer_feedback(suggestion: str, allergy_concern: str):
    feedback = CustomerFeedback(suggestion=suggestion, allergy_concern=allergy_concern)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

# Example
#if __name__ == "__main__":
    # Sample data
#    add_seasonal_flavor("Pumpkin Spice", 22)
#    add_ingredient("Cocoa Powder", 500)
#    add_customer_feedback("Add a vegan option", "Peanut allergy")