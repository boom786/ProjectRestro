from django.urls import path

from home.views import (
    home,
    
    tagpage,
    
    adddish,

    menuPage,

    cart,

    crop_icon_image,
    add_dish_image_icon, 
    
    crop_major_image,
    add_dish_image_major,
    
    crop_secondary_image,
    add_dish_image_secondary,
    
    crop_tertiary_image,
    add_dish_image_tertiary,
    
    edit_dish,
    delete_dish,

    dish_page,
)

#Home Urls
urlpatterns = [
    path("", home, name='home'),

    path("add_tag/",tagpage, name="addtag"),

    path('add_dish/', adddish, name="addDish"),

    path("menu_page/", menuPage, name="menuPage"),

    path("cart/", cart, name="cart"),

    path('add_dish/addIconImage/<dish_id>',add_dish_image_icon , name="addIconImage"),

    path('dish/<dish_id>/', dish_page, name = 'dishPage'),
    
    path('add_dish/addIconImage/<dish_id>/cropIconImage/',crop_icon_image, name="crop_icon_image" ),

    path('add_dish/addMajorImage/<dish_id>',add_dish_image_major , name="addMajorImage"),
    path('add_dish/addMajorImage/<dish_id>/cropMajorImage/',crop_major_image, name="crop_major_image" ),

    path('add_dish/addSecondaryImage/<dish_id>',add_dish_image_secondary , name="addSecondaryImage"),
    path('add_dish/addSecondaryImage/<dish_id>/cropSecondaryImage/',crop_secondary_image, name="crop_secondary_image" ),

    path('add_dish/addTertiaryImage/<dish_id>',add_dish_image_tertiary , name="addTertiaryImage"),
    path('add_dish/addTertiaryImage/<dish_id>/cropTertiaryImage/',crop_tertiary_image, name="crop_tertiary_image" ),

    path('edit_dish/<dish_id>/', edit_dish, name="editDish"),

    path('edit_dish/<dish_id>/delete', delete_dish, name="deleteDish"),

    
]
