This is a project meant to familiarize you with shell input and output redirections and filters. We will cover several commands that display the text of a file such as head, tail, sort. Additionally we will make use of special characters such as the # for comments, | for pipelines, and <> for input and output redirection. When these operators are linked together they can be extremely powerful with the right commands. For example, one often used pipeline is:
    
     $ls -l | less

This command lists all files and directories of current working directory in long format, but makes the ouput scrollable as it does when the less command is used.