# General information
This project is currently heavily work in progress. 
Everything is a subject to change or total refactor without any backward-compatibility. 
Use or test at your own risk.

# Project structure

- **threedverse-django** - Contains backend service which will have RESTful API for frontend application and
other apps that would like to use the data found there.

- **threedverse-frontend** - is a web and mobile frontend which will be a first service for users to use.

# General plan and direction

Main issues this project wants to address:

- Allow users to self host 3D projects they find and create sort of private library
- Project will be a base for cloud storage to show off your creation
- Integration with apps like Cura/PrusaSlicer/Octoprint
- Full integration with OpenSCAD and customization that it allows
- Ability to add source of the model with clear distinction of when it is available and when it is not
    - Integration with fusion360 to publish?
- Automatic generation of preview images + 3D Preview in the browser 
(with fallback for full 360* Images for browsers/clients incapable of presenting 3d content?)
- Further into development allowing users to offer paid models alongside their free models
- Fully customizable profile as a portfolio of your projects 
- Emphasize on the standarization on how to present 3D model in comparable way in list views 
    - Essentially attempting to disallow custom thumbnails that tell absolutely nothing on how the model really looks like (renders and the like)
- Integration with slicers could show statistics on how users choose parameters for printing for given materials and printers
- Gamification of showing off your prints? As part of expanding the gallery of the model to see how people make the models
- Proper support for multi-part prints with ability to create tree-like structure for 3d models storage and presentation
    - Example: Whole model consists of 3 parts, and the model view clearly shows what should be connected to what
    - this is hard but could really help multi-part modelling grow
    
# Choices

- Frontend uses Vue and Quasar.dev (both new in my stack)
- Backend uses plain good old Django + Django Rest Framework + Poetry for packages (new in my stack)

If anyone has better proposition please motivate so.


    
