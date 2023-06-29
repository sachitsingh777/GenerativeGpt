import React, { useState } from 'react';
import { Box, Input, Button, Select, Textarea, Flex } from '@chakra-ui/react';

const App = () => {
const [inputValue, setInputValue] = useState('');
const [outputValue, setOutputValue] = useState('');
const [selectedLanguage, setSelectedLanguage] = useState('');

const handleInputChange = (event) => {
setInputValue(event.target.value);
};

const handleLanguageChange = (event) => {
setSelectedLanguage(event.target.value);
};

const handleConvertClick = async () => {

  
  try {
    const response = await fetch('https://code-convertor-sslj.onrender.com/convert', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
       input: inputValue,
        language: selectedLanguage,
      }),
    });

    const data = await response.json();
    setOutputValue(data);
  } catch (error) {
    console.error('Error:', error);
  }
};

const handleDebugClick = async () => {
  try {
    const response = await fetch('https://code-convertor-sslj.onrender.com/debug', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        input: inputValue,
      }),
    });

    const data = await response.json();
    setOutputValue(data);
  } catch (error) {
    console.error('Error:', error);
  }
};

const handleQualityCheckClick = async () => {
  try {
    const response = await fetch('https://code-convertor-sslj.onrender.com/quality', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        input: inputValue,
      }),
    });

    const data = await response.json();
    setOutputValue(data);
  } catch (error) {
    console.error('Error:', error);
  }
};

return (
<Flex
 
   alignItems="center"
   justifyContent="center"
   bgGradient="linear(to-r, teal.400, cyan.600)"
 >
<Box
     p={4}
     borderRadius="md"
     boxShadow="0 8px 32px 0 rgba(31, 38, 135, 0.37)"
     bg="rgba(255, 255, 255, 0.15)"
     backdropFilter="blur(4px)"
     border="1px solid rgba(255, 255, 255, 0.18)"
     display="flex"
     flexDirection="column"
     alignItems="center"
   >
<Flex direction="column" mb={4}>

<Flex><Select
         value={selectedLanguage}
         onChange={handleLanguageChange}
         placeholder="Select language"
         width="300px"
         mb={2}
         bg="white"
       >
<option value="javascript">JavaScript</option>
<option value="python">Python</option>
<option value="java">Java</option>
{/* Add more language options as needed */}
</Select>
<Button
onClick={handleConvertClick}
mr={2}
colorScheme="teal"
_hover={{ bg: 'teal.500' }}
>
Convert
</Button>
<Button
onClick={handleDebugClick}
mr={2}
colorScheme="teal"
_hover={{ bg: 'teal.500' }}
>
Debug
</Button>
<Button
onClick={handleQualityCheckClick}
colorScheme="teal"
_hover={{ bg: 'teal.500' }}
>
Quality Check
</Button>
</Flex>
</Flex>
<Flex>
<Box
         width="600px"
       
         mr={4}
         p={2}
         bg="white"
         borderRadius="md"
       >
        <Textarea
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        placeholder="Enter your code here"
        width="100%"
       
        bg="teal.50"
        _focus={{ bg: 'teal.100' }}
        borderRadius="md"
        boxShadow="inset 0 0 6px rgba(0, 0, 0, 0.3)"
        ></Textarea>

</Box>
<Box
         width="600px"
        
         p={2}
         bg="white"
         borderRadius="md"
       >
<Textarea
value={outputValue}
readOnly
placeholder="Output"
rows={8}
resize="none"
boxShadow="inset 0 0 6px rgba(0, 0, 0, 0.3)"
width="100%"

bg="teal.50"
_focus={{ bg: 'teal.100' }}
borderRadius="md"
/>
</Box>
</Flex>
</Box>
</Flex>
);
};

export default App;