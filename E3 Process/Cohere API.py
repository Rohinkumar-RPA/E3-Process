import cohere

co = cohere.Client('IwxtBswfFr2GTUvRNFiFkWmwnqTt1CwBGJ0OeYMd')

response = co.generate(
    prompt="Draft a detailed mail on sustainability initiative onboarding for finance department addressing to Rohinkumar without subject",
)

generated_text = response
print(generated_text[0])
