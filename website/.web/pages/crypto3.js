import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Divider, Heading, HStack, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Spacer, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <HStack alignItems={`flex-start`} sx={{"transition": "left 0.5s, width 0.5s", "position": "relative"}}>
  <Box sx={{"display": ["none", "none", "block"], "minWidth": "20em", "height": "100%", "position": "sticky", "top": "0px", "borderRight": "4px solid black"}}>
  <VStack sx={{"height": "100dvh"}}>
  <HStack sx={{"width": "100%", "borderBottom": "4px solid black", "padding": "0", "borderWidth": "medium", "borderRadius": "3px", "borderColor": "pink", "margin": "3%"}}>
  <Box>
  <Box>
  <Image src={`/logo2.png`} sx={{"height": "3em", "marginLeft": "4%"}}/>
</Box>
</Box>
</HStack>
  <VStack alignItems={`flex-start`} sx={{"width": "100%", "overflowY": "auto", "padding": "1em"}}>
  <Link as={NextLink} href={`/`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/home") || (((state.router.page.path === "/") && "Home") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/home") || (((state.router.page.path === "/") && "Home") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Home`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/a-example`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/a-example") || (((state.router.page.path === "/") && "A-Example") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/a-example") || (((state.router.page.path === "/") && "A-Example") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`A-Example`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/crypto1`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/crypto1") || (((state.router.page.path === "/") && "Crypto1") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/crypto1") || (((state.router.page.path === "/") && "Crypto1") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Crypto1`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/crypto2`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/crypto2") || (((state.router.page.path === "/") && "Crypto2") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/crypto2") || (((state.router.page.path === "/") && "Crypto2") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Crypto2`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/crypto3`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/crypto3") || (((state.router.page.path === "/") && "Crypto3") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/crypto3") || (((state.router.page.path === "/") && "Crypto3") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Crypto3`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/crypto4`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/crypto4") || (((state.router.page.path === "/") && "Crypto4") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/crypto4") || (((state.router.page.path === "/") && "Crypto4") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Crypto4`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/profile`} sx={{"_hover": {"text-decoration": "none"}, "width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/profile") || (((state.router.page.path === "/") && "Profile") === "Home")) ? `teal` : `rgb(21,24,51)`, "_hover": {"color": "hotpink"}, "color": isTrue((state.router.page.path === "/profile") || (((state.router.page.path === "/") && "Profile") === "Home")) ? `white` : `white`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/github.svg`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Profile`}
</Text>
</HStack>
</Link>
</VStack>
  <Spacer/>
</VStack>
</Box>
  <Box sx={{"paddingTop": "5em", "paddingX": ["auto", "2em"], "width": "100%"}}>
  <Box sx={{"width": "100%", "alignItems": "flex-start", "boxShadow": "0px 0px 0px 1px rgba(23, 25, 45, 1)", "borderRadius": "0.375rem", "padding": "1em", "marginBottom": "2em"}}>
  <VStack justifyContent={`space-between`} sx={{"borderWidth": "thick", "borderColor": "DA338C", "width": "100%", "bg": "", "borderRadius": "3px"}}>
  <Heading sx={{"fontSize": "3em", "color": "white"}}>
  {`Ripple`}
</Heading>
  <Text sx={{"color": "white"}}>
  {`Welcome to the Ripple Trading page`}
</Text>
  <HStack>
  <Box sx={{"borderWidth": "thick", "borderColor": "pink", "borderRadius": "3px"}}>
  <Image src={`/ripplegraph.png`} sx={{"width": "600px", "height": "auto"}}/>
</Box>
  <Box sx={{"borderWidth": "thick", "borderColor": "#990000", "borderRadius": "3px", "paddingLeft": "8%", "bg": "#404040", "width": "300px"}}>
  <Text sx={{"color": "white"}}>
  {`some data`}
</Text>
  <Button onClick={(_e) => addEvents([Event("state.app_state.change_text", {id:3})], (_e))}>
  {state.app_state.btn_text}
</Button>
</Box>
</HStack>
  <Divider sx={{"borderWidth": "5px"}}/>
  <HStack sx={{"paddingTop": "5%"}}>
  <Box sx={{"borderWidth": "thick", "borderColor": "pink", "borderRadius": "3px"}}>
  <Image src={`/tableEx.jpeg`} sx={{"width": "500px", "height": "auto"}}/>
</Box>
  <Box sx={{"borderWidth": "thick", "borderColor": "#990000", "borderRadius": "3px", "paddingLeft": "8%", "bg": "#404040", "width": "300px"}}>
  <Text sx={{"color": "white"}}>
  {`some data`}
</Text>
</Box>
</HStack>
</VStack>
</Box>
</Box>
  <Spacer/>
</HStack>
  <NextHead>
  <title>
  {`Crypto3`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}
