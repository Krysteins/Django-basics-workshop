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