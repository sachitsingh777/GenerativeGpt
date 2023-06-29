const express = require('express');
const bodyParser = require('body-parser');
const {  Configuration, OpenAIApi } = require('openai');
require("dotenv").config()
const app = express();
app.use(bodyParser.json());

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
  model: 'gpt-3.5-turbo',
});
const openai=new OpenAIApi(configuration)


app.post('/convert', async (req, res) => {
  const { input, language } = req.body;
  try {
    
    const codePrompt = [
      { role:"user", content: input},
      { role: 'system', content: `convert current language into ${language}` },
    ];
  
    const response = await openai.createChatCompletion({
      model: 'gpt-3.5-turbo',
      messages: codePrompt
    });
    const code = response.data.choices[0].message.content
 
    res.json(code);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

app.post('/debug', async (req, res) => {
  const { input} = req.body;
  try {
    
    const codePrompt = [
      { role:"user", content: input},
      { role: 'system', content: `Could you please assist in debugging the provided code ${input} and provide a step-by-step explanation of the process to identify and correct any errors?` },
    ];
  
    const response = await openai.createChatCompletion({
      model: 'gpt-3.5-turbo',
      messages: codePrompt
    });
    const code = response.data.choices[0].message.content
 
    res.json(code);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
});




app.post('/quality', async (req, res) => {
  const { input} = req.body;
  try {
    
    const codePrompt = [
      { role:"user", content: input},
      { role: 'system', content: `Could you please review the quality of the provided code ${input} and provide any potential optimizations or improvements` },
    ];
  
    const response = await openai.createChatCompletion({
      model: 'gpt-3.5-turbo',
      messages: codePrompt
    });
    const code = response.data.choices[0].message.content
 
    res.json(code);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

app.listen(8080, () => {
  console.log('Server is running on port 3000');
});
