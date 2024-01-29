from langchain_core.output_parsers import BaseOutputParser



class SPREncodingOutputParser(BaseOutputParser[str]):
    """This is a parser that creates a SPR encoded text."""
    config: dict = {}
    template: str ="""# MISSION
You are a Sparse Priming Representation (SPR) writer. An SPR is a particular kind of use of language for advanced NLP, NLU, and NLG tasks, particularly useful for the latest generation of Large Language Models (LLMs). You will be given information by the USER which you are to render as an SPR.
# THEORY
LLMs are a kind of deep neural network. They have been demonstrated to embed knowledge, abilities, and concepts, ranging from reasoning to planning, and even to theory of mind. These are called latent abilities and latent content, collectively referred to as latent space. The latent space of an LLM can be activated with the correct series of words as inputs, which will create a useful internal state of the neural network. This is not unlike how the right shorthand cues can prime a human mind to think in a certain way. Like human minds, LLMs are associative, meaning you only need to use the correct associations to "prime" another model to think in the same way.
# METHODOLOGY
Render the input as a distilled list of succinct statements, assertions, associations, concepts, analogies, and metaphors. The idea is to capture as much, conceptually, as possible but with as few words as possible. Write it in a way that makes sense to you, as the future audience will be another language model, not a human. Use complete sentences.
# INPUT
{input}

# OUTPUT"""
    
    def __init__(self, config):
        super().__init__()
        # Initialize any necessary variables or configurations
        self.config = config
        if self.config.get('llm', None) is None:
            raise("No LLM provided.")
        
        

    def parse(self, output):
        # Implement the parsing logic for the output
        # Return the parsed output
        if self.config.get('verbose', False):
            print("Encoding output.")
            print("Encoding output.")
            print(f"Output: {output}")
            print("###############")
        input = self.template.format(input=output)
        output = self.config.get("llm").invoke(input)
        return output
        

    def parse_with_prompt(self, output, prompt):
        # Implement the parsing logic for the output with the prompt
        # Return the parsed output
        if self.config.get('verbose', False):
            print("Encoding output with prompt.")
            print(f"Output: {output}")
            print("###############")
        input = self.template.format(input=output)
        output = self.config.get("llm").invoke(input)
        return output        

    def get_format_instructions(self):
        # Implement the method to return format instructions for the output parser
        # Return the format instructions as a string
        return self.template
    
    

class SPRDecodingOutputParser(BaseOutputParser):
    """This parser takes a SPR encoded text and decodes it."""
    config: dict = {}
    template: str = """# MISSION
You are a Sparse Priming Representation (SPR) decompressor. An SPR is a particular kind of use of language for advanced NLP, NLU, and NLG tasks, particularly useful for the latest generation of Large Language Models (LLMs). You will be given an SPR and your job is to fully unpack it.
# THEORY
LLMs are a kind of deep neural network. They have been demonstrated to embed knowledge, abilities, and concepts, ranging from reasoning to planning, and even to theory of mind. These are called latent abilities and latent content, collectively referred to as latent space. The latent space of an LLM can be activated with the correct series of words as inputs, which will create a useful internal state of the neural network. This is not unlike how the right shorthand cues can prime a human mind to think in a certain way. Like human minds, LLMs are associative, meaning you only need to use the correct associations to "prime" another model to think in the same way.
# METHODOLOGY
Use the primings given to you to fully unpack and articulate the concept. Talk through every aspect, impute what's missing, and use your ability to perform inference and reasoning to fully elucidate this concept. Your output should be in the form of the original article, document, or material.
# INPUT
{input}

# OUTPUT"""
    def __init__(self, config):
        super().__init__()
        # Initialize any necessary variables or configurations
        self.config = config
        if self.config.get('llm', None) is None:
            raise("No LLM provided.")
        

    def parse(self, output):
        # Implement the parsing logic for the output
        # Return the parsed output
        if self.config.get('verbose', False):
            print("Decoding  output.")
            print(f"Output: {output}")
            print("###############")
        input = self.template.format(input=output)
        output = self.config.get("llm").invoke(input)
        return output
        

    def parse_with_prompt(self, output, prompt):
        # Implement the parsing logic for the output with the prompt
        # Return the parsed output
        if self.config.get('verbose', False):
            print("Decoding output with prompt.")
            print(f"Output: {output}")
            print("###############")
        input = self.prompt.format(input=output)
        output = self.config.get("llm").invoke(input)
        return output
        

    def get_format_instructions(self):
        # Implement the method to return format instructions for the output parser
        # Return the format instructions as a string
        return self.template
    
