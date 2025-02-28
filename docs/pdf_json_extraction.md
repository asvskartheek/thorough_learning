# Extract the JSON from PDF 

## Attempt 1
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

<b>Observations</b>
- chapter_text looks like it is verbatim (<span style="color:red">TODO: need to thoroughly check</span>)
- example solutions are definitely summarised (Checked the first one and it is summarised.)