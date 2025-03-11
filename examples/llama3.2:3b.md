
@rescui/use-glow-hover Documentation
====================================

## glowHoverEffect

### Description


useGlowHoverEffect
### Parameters

### Return Value

####  glowHoverEffect

##### Type


Function
##### Description


A function that returns a Glow Hover effect function. The returned function takes an HTMLElement as its argument and returns the Glow Hover effect function.
### Example Use
```js 
{
  const hoverElement = document.getElementById('hoverElement');
  const hoverEffect = useGlowHover({
    size: 100,
    opacity: 0.5,
  });
  hoverEffect(hoverElement);
}
```
### Test Cases

#### Basic usage

##### Description



##### Code
```js 
{
  import { useGlowHover } from "@rescui/use-glow-hover";

  const MyComponent = () => {
    return <div id="hoverElement" style={{
      padding: "10px",
      background: "#333",
      color: "#fff"
    }}></div>
  };

  const hoverEffect = useGlowHover({
    size: 100,
    opacity: 0.5,
  });
  return (<MyComponent /></MyComponent>
,
```

 --- 

#### Customizing the effect

##### Description



##### Code
```js 
{
  import { useGlowHover } from "@rescui/use-glow-hover";

  const MyComponent = () => {
    return <div id="hoverElement" style={{
      padding: "10px",
      background: "#333",
      color: "#fff"
    }}></div>
  };

  const hoverEffect = useGlowHover({
    size: 100,
    opacity: 0.5,
    duration: 500,
  });
  return <MyComponent /></MyComponent>
,
```

 --- 

## useGlowHover

### Description


Use the `useGlowHover` hook to add a hover effect to an HTML element.
### Parameters

#### disabled

##### Type


boolean
##### Description


A boolean indicating whether the effect should be disabled.

 --- 

#### options

##### Type


object
##### Description


An options object that can contain the following properties:
### Return Value

#### ref

##### Type


MutableRefObject<HTMLElement>
##### Description


A mutable reference to the element on which the effect is applied.
### Example Use
```js 
const ref = useGlowHover({ enabled: true });
```
### Test Cases

#### enabled

##### Description


Test the effect when enabled.
##### Code
```js 
import { useGlowHover } from '@rescui/use-glow-hover';

const ref = useGlowHover({ enabled: true });

// Add a class to the element on hover.
ref.current.addEventListener('mouseover', () => {
  ref.current.classList.add('active');
});

// Remove the class when leaving the element.
ref.current.addEventListener('mouseout', () => {
  ref.current.classList.remove('active');
});
```