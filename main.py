from db_handler.models import user, pets, inventory, items, variants

pet = pets.get_by_id(pets.create_pet(owner_id=1, docent_id=1)).kill()
