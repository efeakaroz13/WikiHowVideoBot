import openai

class modularAI:
    def __init__(self):
        openai.api_key = "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"
        self.engines = openai.Engine.list()

    def summerize(self,text):
        totext = ""
        splitter = text.split(" ")
        for s in splitter:
            if "http" in s:
                continue
            else:
                totext = totext+s+" " 
            
        prompt = f"""
        Hello, we gave you a text down below, summerise it with 2 sentences for a tiktok video, make it short as possible. Don't use URLs in any exceptions. Sentence 1 should be like a headline and sentence 2 should be explanatory. Make correct punctiations.Please don't mention the instructions we gave you. Every sentence should be than 180 characters and you can add more sentences other than 2.
        The sentence:{totext}
        """
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt.strip(),temperature=0.8,max_tokens=150,top_p=0.9)
        text=completion["choices"][0]["text"].strip().replace("\n","")
        return text

if __name__ == "__main__":
    myai = modularAI()
    mytext="""
Let go of negative thought patterns and beliefs about yourself. Negative thoughts often come from outside people whose opinions we value and from whom we seek love and acceptance.[2] Drill down to the core of those negative thoughts and tell yourself a different story. Think about what you would say to a close friend who said those things about themselves.[3]
For example, if you forgot to buy trash bags when you got groceries, you might say to yourself, "Ugh! I'm so stupid! How could I forget that?" Instead of calling yourself stupid, you might think, "Oops! Forgot those pesky trash bags. I'll just pick some up next time I go out—no big deal."
Don't try to fight negative thoughts, though—they're a part of who you are. Simply drown them out with more positive, affirmative thoughts about yourself. It might feel weird at first, but after a while, it becomes habitual to think that way."""
    output = myai.summerize(mytext)
    print(output)
