import requests
import os

url = "https://media-api-proxfyprug.s3-accelerate.amazonaws.com/49467801-51c3-4f65-8f1c-d1f3b620d804/out/allclean.mp3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIA2N2ZL3VQL5IASEAL%2F20230511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230511T102425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAN7FncLJjHHfBhy4EGAgOCcBNxctdySJuu0eUoRgQiDAiALcutdLhZhjBcqjkY584nlWf8mkh%2FoxNlILhb4oackxCqUAwij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAQaDDcxNjkxMDA5MTYxNiIMxizIda6R4elWTk3xKugCPBu6OdCo39RCFjSQJq%2F9Q5%2FhAp5Ri29U4KGXSptM45tn3misaO5nOFxi0rApI%2B4%2BIckGw%2BexWvQH60SclBw58JCMUNZSWWHqzhfrWheXQ4F7I0z2TOatdBp1Sc%2B1H02XosQXNHCnTfb7Gcs6dSi%2FQwLA%2FukoevVnpffJJw%2Bh2D5mTRFX5ct2s%2FQBprr85jh%2FLIOVRT01TGI4w8xa4yBcBXrxZ9UfoN971nZBaMj%2FwFud1hK5Qyei3zyesGdHJFHPBN6YxTjOnemN36MV%2BpNocFlh7QKkJ%2FG0%2F7qogiL4M5mfSUAevSmfBdXhsSUTEzQYEc7lN1rVImzlV41GLKYrdHR5TGW9yzlm2thyAVmklagXTSPnw6PW0kLB%2FicZpzugpnKKYHhNdC0FkyP9%2FRF%2FPzpfRf0XSYDvCLBkybmEtj5Gn0WjWB7vMyJ%2FponA9oy3hG7e%2FyMURhTkSIn1bJqNexHWaAWUbBdaMNz58qIGOp4BclazP73ib9%2FxeGjDIu5IzFsg3zAcRbz42Q8m2jV0d6UJWPYeBsCvMxo4eqIGhEA8cYl8gut68BQ4XKHrinGZAu4Pk6A96INXXXm9MijfwDB4eLt2bd6ZG%2B75aNDSGIyvsfXpczErRuE2WWrJvwqcFWIhu8uU%2Bxil4NCpeqk3G2psZ%2FDCvy%2B3xJGLTsN4FIrz3NGKwAd29bNYnEAIJr4%3D&X-Amz-Signature=d8ecb30f70f1f18742530836f75f0c14e08cd39855306a684b9a1859e7a03f81&X-Amz-SignedHeaders=host&x-id=GetObject"

response = requests.get(url)

if response.status_code == 200:
    # Extract the filename from the URL
    filename ="audio.mp3"

    # Prompt the user to select a destination directory
    destination_dir = "E:/"

    # Construct the full output path
    output_path = os.path.join(destination_dir, filename)

    # Save the downloaded file
    with open(output_path, "wb") as output_file:
        output_file.write(response.content)
        print(f"File saved successfully at: {output_path}")
else:
    print("Failed to download the file.")
