import { useRef, useState } from "react";
import {
  Box,
  Button,
  Flex,
  Text,
  Textarea,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
  useDisclosure,
} from "@chakra-ui/react";
import axios from "axios";
import { ChatIcon} from '@chakra-ui/icons'
const init = {
  role: "system",
  content: "I am a food expert from zomato",
};

export const Chatbot = () => {
  const inputRef = useRef(null);
  const [input, setInput] = useState("");
  const [bot, setBot] = useState([init]);
  const { isOpen, onOpen, onClose } = useDisclosure();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const message = { role: "user", content: input };
    const newdata = [...bot, message];

    setBot(newdata);
    try {
      const response = await axios.post(
        "https://api.openai.com/v1/chat/completions",
        {
          model: "gpt-3.5-turbo",
          messages: newdata,
        },
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${process.env.REACT_APP_OPENAI_SECRET}`,
          },
        }
      );

      const chatbotMessage = response.data.choices[0].message.content;
      const updatedChatHistory = [
        ...newdata,
        { role: "assistant", content: chatbotMessage },
      ];

      setBot(updatedChatHistory);
      setInput("");
      inputRef.current.focus();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <Button onClick={onOpen}>
        {/* Add your chatbot icon here */}
        <ChatIcon boxSize={6} />
      </Button>
      <Modal isOpen={isOpen} onClose={onClose} size="lg" >
        <ModalOverlay />
        <ModalContent bg="whiteAlpha.600">
          <ModalHeader>Chatbot</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Flex direction="column" alignItems="center" marginBottom="10">
              <Box as="div" marginTop="2">
                <Box as="div">
                  {bot.map((message, index) => (
                    <Box
                      key={index}
                      as="div"
                      marginTop={index > 0 ? "2" : undefined}
                      backgroundColor={message.role === "user" ? "teal.400" : "#171A26"}
                      color="white"
                      borderRadius="md"
                      padding="3"
                      boxShadow="md"
                    >
                      <Text as="p" fontSize="base">
                        {message.content}
                      </Text>
                    </Box>
                  ))}
                </Box>
              </Box>
              <form onSubmit={handleSubmit}>
                <Flex
                  alignItems="center"
                  as="div"
                  width="130%"
                  margin="auto"
                  marginTop="24"
                >
                  <Textarea
                    as="textarea"
                    mt="40"
                    flex="1"
                    h="12"
                    py="2"
                    px="3"
                    color="black"
                    border="2px"
                    borderColor="gray.300"
                    borderRadius="lg"
                    marginRight="2"
                    outline="none"
                    _focus={{ borderColor: "blue.400" }}
                    placeholder="Ask a question..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    ref={inputRef}
                    style={{ width: "90%" }}
                  />
                  <Box width="20" mt="40">
                    <Button
                      type="submit"
                      w="full"
                      py="2"
                      px="4"
                      bg="black"
                      color="white"
                      borderRadius="lg"
                      textAlign="center"
                      outline="none"
                      _hover={{ bg: "gray.800" }}
                    >
                      Send
                    </Button>
                  </Box>
                </Flex>
              </form>
            </Flex>
          </ModalBody>
          {/* You can include a footer if needed */}
          {/* <ModalFooter>
            <Button onClick={onClose}>Close</Button>
          </ModalFooter> */}
        </ModalContent>
      </Modal>
    </>
  );
};
