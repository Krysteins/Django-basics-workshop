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

