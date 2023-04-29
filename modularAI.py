import openai

class modularAI:
    def __init__(self):
        openai.api_key = "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"
        self.engines = openai.Engine.list()

    def summerize(self,text):
        prompt = f"""
        Hello we are a tiktok channel and we will use the text below for our video in just 5-10 seconds of it. Summerize the text below like a headline. You need to gain interest from user. Make it like first explanatory sentence and then a little description sentence. Make it short as possible with 2 sentences.
        Use basic words for everyone to understand.
        The sentence:{text}
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
