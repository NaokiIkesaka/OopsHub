'use client';

import Image from "next/image";
import { useEffect, useState } from "react";
import React, { ChangeEvent } from "react";
import {Box,Text} from "@chakra-ui/react";
import { Heading } from "@chakra-ui/react";
import { Button } from "@chakra-ui/react";
import { Textarea } from "@chakra-ui/react";
import { Input } from "@chakra-ui/react"

export default function Home() {

let [title, setTitle] = useState("");
let [text, setText] = useState("");

let handleInputChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    let inputValue = e.target.value;
    setText(inputValue);
}

let handleTitleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setTitle(e.target.value);
}
return (
    <>
    <Box maxW='32rem'>
    <Heading mb={4}>失敗談共有アプリ</Heading>
    <Text fontSize='xl'>
        失敗談を共有する事ができるアプリです😃
    </Text>
    <Text mt="30px">失敗談を編集する</Text>
    <Text mt="20px">タイトル：{title}</Text>
    <Input
    onChange={handleTitleChange}/>
    <Text mb='8px'>失敗談：{text}</Text>
    <Textarea
        value={text}
        onChange={handleInputChange}
    />
    <Button 
    size='lg' 
    colorScheme='green' 
    mt='24px'
    as="a"
    href="">
        編集
    </Button>
    </Box>
    </>
);
}