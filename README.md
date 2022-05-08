# Django basics workshop

# Workshop &ndash; Base template

** HTML ** base template. It will be the base on which we will create new subpages.
The template contain:
1. page title,
2. menu with redirects to the following pages:
     * list of all rooms (home page),
     * functionality of adding a new room,
3. footer with information about the author of the project.

# Workshop &ndash; Model of the hall

Add a model to represent the room. It stores information such as:
* room name (text field, max 255 characters, unique),
* room capacity (integer numeric type field),
* availability of the projector (field type `boolean`).

# Workshop &ndash; The view of adding a room

Create a view that allows to add a new room. Place it at `/ room / new /`.
The view:
* after entering the ** GET ** method, display a form with the following fields:
     * name of the room &ndash; text,
     * room capacity &ndash; number,
     * projector availability &ndash; checkbox.
* after entering using the ** POST ** method:
     * if the name of the room is not empty,
     * if the room with the given name no longer exists in the database,
     * if the capacity of the room is a positive number;
     * if the data is correct, save the new room to the database and redirect the user to the home page,
     * if they are incorrect, it should display an appropriate message to the user.

# Workshop &ndash; List of all rooms

A view that lists all available rooms.
If there is no room in the database, the following message be displayed:
** "No rooms available" **.

The following information be displayed:
* name of the room &ndash; be a link redirecting to a page with a detailed view of the room (`/ room / {id} /`),
* room capacity,
* room availability (information if the room is occupied),
* projector availability,
* edit button &ndash; redirecting to the room edition page (`/ room / modify / {id} /`).
* delete button &ndash; redirecting to the page deleting the room (`/ room / delete / {id}`).
* button book &ndash; redirecting to the room registration form (`/ room / reserve / {id}`).

# Workshop &ndash; Removing a room

The view only supports the ** GET ** method.

View :
* is available at `/ room / delete / {id}`,
* based on the `id` parameter passed in the address, searches for a room and remove it
* finally, it redirects the user to a list of all available rooms.


# Workshop &ndash; Modification of the hall

A view that allows you to modify the parameters of the room.

View:
* is available at `/ room / modify / {id}`,
* after entering with the ** GET ** method, he searches for a room, based on the `id` parameter provided in the address
    and then display the form that allows you to edit:
    * names,
    * capacity,
    * projector availability,
* after entering with the ** POST ** method, checks if:
    * capacity is greater than zero,
    * has the name been entered,
    * if there is no room with the given name in the database,
    * if the data is correct, he should save the changes to the database and redirect the user to the list of all rooms,
    * if they are incorrect, he should inform the user about it

# Workshop &ndash; Booking model

Room booking model. Represents the room reservation for the day.
It stores the following data:
* date,
* room id,
* comment added when booking.

It is linked to the room model by the relationship: one room can have multiple all-day bookings (each on a different day).
When a room is deleted, its reservations are deleted.


# Workshop &ndash; Reservation view

Room reservation view. View:
* is available at `/ room / reserve / {id}`, where `id` is the room id,
* after entering with the ** GET ** method, it displays a form with the following fields:
     * comment,
     * date selection field,
* after entering using the ** POST ** method:
     * verifies that the room on a given day is not already booked,
     * checks if the date is not from the past,
     * save the room reservation,
     * redirect the user to the list of all rooms.

# Workshop &ndash; Detailed view of the hall

A view that shows detailed information about the room.
View:
* displays all the data about the room:
     * name,
     * capacity,
     * projector availability,
* view all future room reservations, including comments.

Provides links to:
* room edition pages,
* pages of removing the room,
* room booking site.

Reservations are sorted from the oldest.
