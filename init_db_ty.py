__author__ = 'Ty Anderson'

# Initialize Django
import os
# Sprint2 is the name of my project
os.environ['DJANGO_SETTINGS_MODULE'] = 'Sprint2.settings'
import django
django.setup()

# Other imports
import homepage.models as hmod

# Delete all previous data, so that I can start off with a fresh new database

# Delete users
hmod.User.objects.all().delete()

# Delete items
hmod.Sale_Product.objects.all().delete()

# Delete Photographs
hmod.Photograph.objects.all().delete()

# Create Admin account
for data in [
    ["Admin", "Admin", "admin", "admin", True],
]:
    # Create new user
    u = hmod.User()

    # Assign user attributes
    u.first_name = data[0]
    u.last_name = data[1]
    u.username = data[2]
    u.set_password(data[3])
    u.is_superuser = data[4]
    u.save()

    # Add user to group 3 (Admin)
    u.groups.add(3)

    # Add user permissions
    # u.user_permissions.add(1)


# Create Manager account
for data in [
    ["Manager", "Manager", "manager", "manager", False],
]:
    # Create new user
    u = hmod.User()

    # Assign user attributes
    u.first_name = data[0]
    u.last_name = data[1]
    u.username = data[2]
    u.set_password(data[3])
    u.is_superuser = data[4]
    u.save()

    # Add user to group 2 (Manager)
    u.groups.add(2)

    # Add user permissions
    # u.user_permissions.add(1)

# I'll need to create the auth_groups of user, manager, and admin too

# Create the photos for the new items
for data in [
    ["Wand", "/store/media/wand.jpg"],
    ["GoveRobes", "/store/media/gove.jpg"],
    ["Quill", "/store/media/quill.jpg"],
]:
    # Create new Sale Product
    p = hmod.Photograph()

    # Assign product attributes
    p.description = data[0]
    p.image = data[1]
    p.save()

# Create Sale Products
for data in [
    ["10", "C-10.5", "10", 10, "Harry Potter", "Wand", "Wand used in filming of Harry Potter.", "C7415", 4.00, 1],
    ["2", "D-5.1", "", 249.99, "Gove Allen", "Robe of Sir Gove", "Professor Gove's very own robe.", "C4516", 184.99, 2],
    ["100", "C-7.1", "5", 0.99, "Maker Inc.", "Quill", "Writing quill.", "C4111", .41, 3],
]:
    # Create new Sale Product
    p = hmod.Sale_Product()

    # Assign product attributes
    p.quantity_on_hand = data[0]
    p.shelf_location = data[1]
    p.production_time = data[2]
    p.price = data[3]
    p.manufacturer = data[4]
    p.name = data[5]
    p.description = data[6]
    p.serial_number = data[7]
    p.value = data[8]
    p.photo_id = data[9]
    p.save()

