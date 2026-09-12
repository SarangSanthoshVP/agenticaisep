def ask_gemini_python(topic, lines):

    prompt = f"Hey, can help me write a sample program on {topic}, and write it in {lines} lines"

    print(prompt)


ask_gemini_python("loops", 10)
ask_gemini_python("functions", 15)

# Hey, can help me write a sample program on loops, and write it in 10 lines
# Hey, can help me write a sample program on functions, and write it in 15 lines