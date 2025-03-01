# Extract the JSON from PDF 

## Attempt 1
- 1 Mar, 2025 12:02AM
- I used o3-mini hosted on chat.com
- attached the [PDF file](../data/raw_pdf_files/math_11_ch6_pnc.pdf)
- turned on the reasoning mode
- prompt:
```
this is PDF of a chapter from my math textbook. can u go through it all and convert into the following JSON file:

{
"chapter_name": "",
"chapter_text": "", # this should be combined parts of all the theory/text from the chapter. do not include examples or exercise questions
"example_problems": [{
"question": "",
"reasoning": "",
"answer": "" # just the final answer
}], # list of all worked out examples in the text
"exercises" : [{
"question" : "",
"answer" : "", # leave this blank we will fit this one later.
}] # list of all the exercise questions in the chapter
}
```
- [Output](../data/extracted_jsons/math_11_ch6_pnc_att1.json)

<b>Observations</b>
- chapter_text was summarised
- reasoning in example_problems is also summarised.

## Attempt 2
- 1 Mar, 2025 12:18AM
- tweaked the prompt to send verbatim content

- prompt:
```
this is PDF of a chapter from my math textbook. can u go through it all and convert into the following JSON file:
{
"chapter_name": "",
"chapter_text": "", # this should be combined parts of all the theory/text from the chapter. do not include examples or exercise questions. this should be verbatim text
"example_problems": [{
"question": "",
"reasoning": "", # verbatim reasoning as per the textbook. 
"answer": "" # just the final answer
}], # list of all worked out examples in the text
"exercises" : [{
"question" : "",
"answer" : "", # leave this blank we will fit this one later.
}] # list of all the exercise questions in the chapter
}
```
- [Output](../data/extracted_jsons/math_11_ch6_pnc_att2.json)

<b>Observations</b>
- chapter_text looks like it is verbatim (<span style="color:orange">TODO: need to thoroughly check</span>)
- example solutions are definitely summarised (Checked the first one and it is summarised.)
- also changing the questions in the examples section
    - L36: original question is with expanded version of 5C2.
    - L41: question itself is wrong, did a wrong parsing.

## Attempt 3
- 1 Mar 2025, 1:22AM
- used llama parse premium version (15 credits/1p) to convert into [Markdown](../data/extracted_jsons/math_11_ch6_pnc_att3_llama.md)
- <b>Failed attempt</b>: gave markdown to o3-mini, almost same prompt just changed PDF to markdown at the start. NO RESULT. FAILED HORRIBLY
- <b>Failed attempt</b>: gave markdown to claude 3.5 sonnet, same prompt as o3-mini. Not enough tokens apparently
- <b>Successful attempt?</b>: gave markdown to deepseek (not deepthink r1), same prompt as o3-mini. [OUTPUT](../data/extracted_jsons/math_11_ch6_pnc_att3.json)
    - Had to click on continue thrice, so maybe it might not work for very long chapters.
    - then added solutions manually from the [solutions pdf](../data/raw_pdf_files/math_11_solns.pdf)

<b>Observations</b>
- perfect converting into markdown, need to some processing to get in our required format.
- with deepseek the results look decent, did a high-level rough check (<span style="color:orange">TODO: need to thoroughly check</span>)
- ran [data sanity check](../sanity_check_ch6_data.py) number of exercises is correct, but LLM missed 6 example_problems in the middle. [Examples 17, 18, 19, 20, 21, 22 from the textbook]. All of this data is present in the [extracted markdown](../data/extracted_jsons/math_11_ch6_pnc_att3_llama.md), so deepseek model made the error.