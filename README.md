# Image Format Converter (GUI)

This Python project provides a simple graphical user interface (GUI) to convert image files between PNG and JPG formats using the `Tkinter` and `PIL` (Pillow) libraries.

General view : ![image](https://github.com/user-attachments/assets/705ba610-1a8a-4574-bb18-c7d510478505)

## Features
- **Browse Images**: Allows users to select an image file from their system.
- **Convert PNG to JPG**: Converts PNG images to JPG format.
- **Convert JPG to PNG**: Converts JPG images to PNG format.
- **Error Handling**: Displays informative error and success messages using messageboxes.

## Requirements

To run this project, you need to have Python installed, along with the following libraries:

- **Tkinter**: The standard Python interface to the Tk GUI toolkit. (Usually installed by default with Python).
- **Pillow**: A powerful Python Imaging Library (PIL) fork.
- **Dictionary**: Using the dictionary allows us to dynamically call the appropriate conversion function based on the image format selected by the user.In our project, the dictionary data structure is used to map image formats.

### Install Pillow

You can install Pillow using `pip`. If it's not already installed, you can do so by running the following command in your terminal or command prompt: 

```bash
pip install Pillow

### features
when we start the program ...
General UI: ![image](https://github.com/user-attachments/assets/ba8fb83e-d4c7-414d-bbd9-c8c59036f42e)

now we can select the images from the browser to convert them form
(i) jpg to png and
(ii) png to jpg

this are use the "dictionary datastructure" so the images which are going to be stored in different collections.
(i) to select the image from the browser
--click on the browser

![image](https://github.com/user-attachments/assets/12058b45-ba4e-4d59-afaa-3de78966232c)

as you can see we can select the image form the browser to convert them ...

-- when the image get selected successfully then...

![image](https://github.com/user-attachments/assets/9cb0ccc7-03be-45d0-95e3-e9cc87207be8)

(ii) when we click on png to jpg to select the image which will going to store in another directory cause we are select the dictionary data-structure.

![image](https://github.com/user-attachments/assets/2efc2299-f876-4268-bed7-eac25fa6be89)

if the image is already saved then we get,

![image](https://github.com/user-attachments/assets/839f46b0-1e26-4404-b792-8aa95960178f)

(iii) when we click on jpg to png to select the image which will going to store in another directory cause we are select the dictionary data-structure.

![image](https://github.com/user-attachments/assets/b8390b4c-c91d-43ed-b0f6-2427ed25eb9b)

when the image is converted then we use

![image](https://github.com/user-attachments/assets/776d8c4e-9ce8-40c4-a026-817a6a933f64)

### Additional Sections:

1. **Screenshots**: You can include images of the interface for better user understanding. Save any relevant screenshots under the `images/` folder and link them in the `README.md` as shown.
   
2. **Project Structure**: Clearly lists the files in the project and describes their roles.

3. **Troubleshooting**: Adds helpful tips for users if they encounter problems when running the application.

4. **Contribution Guidelines**: Encourages collaboration and provides instructions on how others can contribute to the project.

This extended `README.md` file will give a comprehensive overview of the project, helping both users and potential contributors.
