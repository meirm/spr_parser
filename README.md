# Sparse Priming Representation Encoder/Decoder

Langchain outputParser implementing a sparse priming representation (SPR) encoder/decoder for text generation. based on the work of David Shapiro

[https://github.com/daveshap/SparsePrimingRepresentations]

The output parser requires an LLM to encode/decode. 

Example of a sparse priming representation (SPR) encoder/decoder for text generation.

User asks LLM to write a biography of Abraham Lincoln. LLM generates a biography of Abraham Lincoln.

```
Query: Write the biography of Abraham Lincoln.
```

The LLM outputs a biography of Abraham Lincoln.

```
Abraham Lincoln (February 12, 1809 – April 15, 1865) was an American statesman and lawyer who served as the 16th President of the United States from March 1861 until his assassination in April 1865. He is considered one of America's greatest heroes because of his leadership during the country's Civil War and for the Emancipation Proclamation that abolished slavery.

Born in Hodgenville, Kentucky, Lincoln grew up in a poor family in a one-room log cabin on the frontier. His formal education was limited to about one year of schooling due to his family's financial constraints and his need to work from a young age. However, he was avid reader throughout his life and became largely self-taught.

Before becoming president, Lincoln held a number of public offices in Illinois, including state legislator, member of the U.S. House of Representatives, and U.S. Senator. He also pursued a career as a lawyer, rising to prominence in his community through his successful legal work and powerful oratory skills.

Lincoln entered the national political scene as a member of the Whig Party, which he left when it dissolved. In 1858, he joined the newly formed Republican Party and was nominated for the U.S. Senate. He lost that race but gained national attention through his famous debates with Democrat Stephen A. Douglas on the issue of slavery's expansion into the western territories.

Lincoln successfully ran for president in 1860, winning the election despite only receiving 39.8% of the popular vote. His victory caused seven southern slave states to secede from the Union before he took office, leading to the start of the American Civil War. Throughout the war, Lincoln navigated a difficult balance between preserving the Union and emancipating the enslaved people. In 1863, he issued the Emancipation Proclamation, which declared that all slaves in Confederate-held territory were to be set free.

Throughout his presidency, Lincoln faced immense pressure from both sides of the conflict and made tough decisions that ultimately led to the Union's victory and the end of slavery in the United States. However, on April 14, 1865, just days after the war ended, he was assassinated by Confederate sympathizer John Wilkes Booth at Ford's Theatre in Washington D.C., making him the first sitting U.S. President to be assassinated.
```

We use the SPR encoder to compress the biography into a short summary.

```
- Abraham Lincoln (1809-1865), 16th US President, hero
- Born poor, frontier Kentucky, limited education
- Avid reader, self-taught
- Illinois public offices, lawyer, orator
- Whig Party member, then Republican
- 1860 presidential election win, southern states secede
- American Civil War, Union/slavery balance
- Emancipation Proclamation (1863)
- Tough decisions, Union victory, end of slavery
- Assassination (April 1865) by John Wilkes Booth
```

We use the SPR decoder to expand the summary into a biography.

```
Abraham Lincoln: The Sixteenth President and the Civil War Hero

Abraham Lincoln, born on February 12, 1809 in a log cabin in Hardin County, Kentucky, was the 16th President of the United States. He is often remembered as one of the greatest heroes in American history for his role in leading the country through its most devastating conflict, the American Civil War, and for his unwavering commitment to abolish slavery.

Lincoln was born into a poor family and received limited formal education. However, he was an avid reader and a self-taught individual who developed his knowledge and skills through independent study and dedication to improving himself. After working in various jobs, Lincoln moved to Illinois where he began his career as a public servant and lawyer. He also honed his oratory skills, becoming a renowned speaker and advocate for the common man.

Initially, Lincoln was a member of the Whig Party before joining the newly formed Republican Party. In 1860, he won the presidential election, although this victory was followed by the secession of southern states who opposed his stance on slavery. These states went on to form the Confederate States of America and initiated the American Civil War in April 1861.

During his presidency, Lincoln faced numerous tough decisions. He issued the Emancipation Proclamation in January 1863, which declared that all slaves within the Confederacy were to be set free. This proclamation not only aimed at weakening the Confederate forces but also marked a significant step towards the abolition of slavery in the United States.

Under Lincoln's leadership, the Union Army fought steadily against the Confederates, ultimately achieving victory in April 1865. The end of the Civil War led to the end of slavery as well, fulfilling one of Lincoln's most significant goals.

Tragically, on April 14, 1865, just days after the war's end, Lincoln was assassinated by Confederate sympathizer John Wilkes Booth at Ford's Theatre in Washington D.C. His death marked a tragic loss for America and the world, but his legacy as a courageous leader and champion of human rights lives on to this day.

Abraham Lincoln's story is one of hard work, determination, and commitment to justice. His leadership during one of America's most challenging periods has left an indelible mark on American history and the struggle for equality and freedom worldwide.
```