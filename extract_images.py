import os
import pypdf

pdf_path = r"c:\MYCLAUDE_PROJECT\SafeGuide\에버랜드 지하철이동경로.pdf"
output_dir = r"c:\MYCLAUDE_PROJECT\SafeGuide\assets"

os.makedirs(output_dir, exist_ok=True)

print("Starting image extraction...")
try:
    reader = pypdf.PdfReader(pdf_path)
    print(f"PDF loaded successfully. Total pages: {len(reader.pages)}")
    
    extracted_count = 0
    for page_num, page in enumerate(reader.pages):
        images = page.images
        print(f"Page {page_num + 1} has {len(images)} images.")
        for count, img in enumerate(images):
            filename = f"extracted_img_{page_num + 1}_{count + 1}.png"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, "wb") as f:
                f.write(img.data)
            
            print(f"Saved: {filename} ({len(img.data)} bytes)")
            extracted_count += 1
            
    print(f"Done! Extracted {extracted_count} images total.")
except Exception as e:
    print(f"Error during extraction: {e}")
