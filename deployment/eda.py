import streamlit as st
import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

# Function to check if file exists
def check_file(file_path):
    if not os.path.exists(file_path):
        st.error(f"File {file_path} not found. Please make sure the file exists in the correct directory.")
        return False
    return True

# Create the main program
def run():
    file_path = 'class_distribution.csv'
    
    # Check if the file exists
    if not check_file(file_path):
        return
    
    # Load the data from the CSV file
    cases_df = pd.read_csv(file_path)

    # Add a title for the Streamlit app
    st.title("Exploratory Data Analysis")
    
    # Add subtitle
    st.write('''Choose what to visualize:''')
    
    # Create a multi-select dropdown for choosing visualization type
    visualization_type = st.multiselect('Select Visualization:', ('Class Distribution', 'Images'))

    if 'Class Distribution' in visualization_type:
        # Create an interactive bar chart with Plotly
        st.subheader('Number of Images in Each Case Category')
        fig = px.bar(cases_df, x='Case Category', y='Number of Images',
                     color='Case Category',
                     labels={'Number of Images': 'Number of Images', 'Case Category': 'Case Category'},
                     height=400,
                     color_discrete_sequence=['lightsteelblue', 'navajowhite', 'lightsalmon'])
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

        # Add additional information if necessary
        st.write('''Diagram batang menunjukkan distribusi gambar untuk lima kategori sayuran.''')
        st.write('''1. **Cabbage**: Kategori ini memiliki 125 gambar, yang menunjukkan fokus signifikan pada penangkapan kondisi kubis.''')
        st.write('''2. **Capsicum**: Terdapat 125 gambar untuk kategori ini, menunjukkan pentingnya penangkapan kondisi capsicum.''')
        st.write('''3. **Carrot**: Kategori ini memiliki 125 gambar, menandakan perhatian yang seimbang terhadap kondisi wortel.''')
        st.write('''4. **Cauliflower**: Terdapat 125 gambar untuk kategori ini, menunjukkan upaya untuk menangkap variasi dalam kondisi kembang kol.''')
        st.write('''5. **Pumpkin**: Kategori ini memiliki 125 gambar, menunjukkan fokus untuk memahami kondisi labu.''')
        st.write('''Distribusi yang seimbang ini diharapkan dapat meningkatkan diagnostik untuk semua kondisi sayuran.''')
    
    if 'Images' in visualization_type:
        
        # Add title
        st.markdown('''### **Image Visualization**''')
        
        # Define the directories for each class
        class_dirs = {'Cabbage': './Image_Sample/Cabbage',
                      'Capsicum': './Image_Sample/Capsicum',
                      'Carrot': './Image_Sample/Carrot',
                      'Cauliflower': './Image_Sample/Cauliflower',
                      'Pumpkin': './Image_Sample/Pumpkin'}

        # Display images and descriptions for each category in separate sections
        for class_name, folder in class_dirs.items():
            st.subheader(f'{class_name} Images')
            image_files = [f for f in os.listdir(folder) if f.endswith(('png', 'jpg', 'jpeg'))][:5]
            fig, axes = plt.subplots(1, len(image_files), figsize=(20, 4))  # Adjust subplot layout as needed

            for idx, image_file in enumerate(image_files):
                img_path = os.path.join(folder, image_file)
                img = Image.open(img_path)
                if len(image_files) > 1:
                    axes[idx].imshow(img)
                    axes[idx].axis('off')
                    axes[idx].set_title(image_file)
                else:
                    axes.imshow(img)
                    axes.axis('off')
                    axes.set_title(image_file)

            plt.tight_layout()
            st.pyplot(fig)

            # Add description for each class after displaying images
            if class_name == 'Cabbage':
                st.write('''Gambar kubis menunjukkan daun-daun dengan permukaan yang halus dan bebas dari kerusakan parah atau pertumbuhan yang tidak teratur.''')
            elif class_name == 'Capsicum':
                st.write('''Gambar capsicum memperlihatkan permukaan yang bersih dan tidak adanya tanda-tanda kerusakan signifikan, menunjukkan kondisi kesehatan yang baik.''')
            elif class_name == 'Carrot':
                st.write('''Gambar wortel menunjukkan permukaan yang halus tanpa tanda-tanda pertumbuhan yang tidak biasa, menandakan kondisi yang sehat.''')
            elif class_name == 'Cauliflower':
                st.write('''Gambar kembang kol menunjukkan distribusi permukaan yang rata dan tidak ada pertumbuhan yang tidak teratur, menunjukkan kondisi yang baik.''')
            elif class_name == 'Pumpkin':
                st.write('''Gambar labu memperlihatkan permukaan yang bersih dan struktur yang sehat, tanpa tanda-tanda kerusakan yang signifikan.''')

# Run the app
if __name__ == '__main__':
    run()
