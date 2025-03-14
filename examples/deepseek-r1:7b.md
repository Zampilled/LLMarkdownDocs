
@rescui/use-glow-hover Documentation
====================================

## useGlowHover

### Description


The `useGlowHover` hook provides a convenient way to add glow effects around elements when they are hovered over. It automatically handles the styling and animations required for smooth transitions.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The element to apply the glow hover effect to.

 --- 

#### disabled

##### Type


boolean
##### Description


If set to true, disables the glow hover effect for this element.

 --- 

#### ...options

##### Type


GlowHoverOptions
##### Description


An object containing various options to customize the glow effect including colors and animation timing.
### Return Value

#### Accessor or Object containing the effect

##### Type


Effect
##### Description


The returned value is an effect that can be used with `useEffect` to trigger the glow hover animation when the element is hovered over.
### Example Use
```ts 
const { disabled, el } = useGlowHover(document.getElementById('myElement'));
```
### Test Cases

#### Basic Setup

##### Description


Test if the effect works without any configuration.
##### Code
```ts 
function Test() {
            const el = document.getElementById('testEl');
            const disabled = false;
            const glowHoverEffect = useGlowHover(el, { disabled });
            
            useEffect(() => {
                el.style.transition = 'all 0.3s ease-in-out';
                setTimeout(() => disableGlowHover(el), 500);
            }, [el]);
        };
        return () => {
            disableGlowHover(el);
        };
     }
```

 --- 

#### Custom Colors

##### Description


Test if custom colors can be used for the glow effect.
##### Code
```ts 
function Test() {
            const el = document.getElementById('testEl');
            const disabled = false;
            const glowHoverEffect = useGlowHover(el, { disabled: true, lightColor: '#ff0000' });
            
            useEffect(() => {
                setTimeout(() => disableGlowHover(el), 500);
            }, [el]);
        };
        return () => {
            disableGlowHover(el);
        };
     }
```

 --- 

#### Animated Transition

##### Description


Test if the animation timing can be adjusted.
##### Code
```ts 
function Test() {
            const el = document.getElementById('testEl');
            const disabled = false;
            const glowHoverEffect = useGlowHover(el, { disabled: true, lightSizeEnterAnimationTime: 0.5, lightSizeLeaveAnimationTime: 0.8 });
            
            useEffect(() => {
                setTimeout(() => disableGlowHover(el), 500);
            }, [el]);
        };
        return () => {
            disableGlowHover(el);
        };
     }
```

 --- 

## GlowHoverHookOptions

### Description


The glowHoverEffect is a React hook that adds a glowing effect around an element when it hovers over. It's designed to enhance user experience by providing visual feedback when interacting with elements on the page.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The element on which this hook is applied.

 --- 

#### hoverBg

##### Type


string | undefined
##### Description


Optional background color for the hover effect. If not provided, the default glow color will be used.

 --- 

#### lightSize

##### Type


number
##### Description


The size of the light when it appears on hover.

 --- 

#### lightSizeEnterAnimationTime

##### Type


number | undefined
##### Description


Optional time in milliseconds to animate the light entering. If not provided, default animation is used.

 --- 

#### lightSizeLeaveAnimationTime

##### Type


number | undefined
##### Description


Optional time in milliseconds to animate the light leaving. If not provided, default animation is used.

 --- 

#### isElementMovable

##### Type


boolean
##### Description


If true, the glow effect will follow mouse movement on the element; if false, it stays relative to the element.

 --- 

#### customStaticBg

##### Type


string | null
##### Description


Optional static background color that doesn't animate. Useful for cases where you want a different look than default.

 --- 

#### forceTheme

##### Type


'light' | 'dark' | false
##### Description


Forces the theme of the glow effect; if set to light or dark, it will automatically adjust parameters based on the current theme.

 --- 

#### enableBurst

##### Type


boolean
##### Description


If true, adds a burst animation when hovering. The default is false.

 --- 

#### mode

##### Type


string | undefined
##### Description


The glow mode can be 'glow' for the default effect or 'sharp' for a more defined glow.

 --- 

#### preset

##### Type


presets.d.ts
##### Description


Preset configuration options that can be used to quickly apply predefined settings.
### Return Value

#### void

##### Type


function
##### Description


The effect function which is called when the element is hovered over.
### Example Use
```ts 
const useGlowHover = require('@react-hooks/use-glow-hover');

export default function MyComponent() {
    const { el, glowHoverEffect } = useGlowHover({ forceTheme: 'dark', enableBurst: true });

    return (
        <div>{el}</div>
    );
}

useEffect(() => {
    // Add the effect when the component mounts
    const observer = new useEffectObserver(el => {
        console.log('Hover happened:', el);
        glowHoverEffect(el);
    });
}, [el]);

```
### Test Cases

#### basicGlowHoverTest

##### Description


Basic test for the default glow effect with all parameters set to their defaults.
##### Code
```ts 
import { useGlowHover } from '@react-hooks/use-glow-hover';

export default function BasicTest() {
    const component = document.createElement('div');
    component.textContent = 'Hello Glow!';
    const { el, glowHoverEffect } = useGlowHover({ forceTheme: 'dark', enableBurst: true });
    
    // Add observer
    const observer = new useEffect(() => {
        return () => {
            glowHoverEffect(el);
        };
    }, [el]);

    document.body.appendChild(component);
    try {
        setTimeout(() => {
            const el = component.firstChild;
            console.log('Hover:', forceTheme, enableBurst);
            expect(el.style.left).toBeWithin(10, 25); // Adjust this expectation based on actual implementation
        }, 1000);
    } catch (error) {
        console.error('Error:', error);
    }
    document.body.removeChild(component);
}

```

 --- 

#### glowHoverWithCustomBgTest

##### Description


Test custom static background color.
##### Code
```ts 
import { useGlowHover } from '@react-hooks/use-glow-hover';

export default function GlowTests() {
    const component = document.createElement('div');
    component.textContent = 'Hello Glow!';
    
    // Apply custom static background
    const options = {
        forceTheme: 'dark',
        enableBurst: true,
        customStaticBg: '#ff0000'
    };
    const { el, glowHoverEffect } = useGlowHover(options);

    // Add observer
    const observer = new useEffect(() => {
        return () => {
            glowHoverEffect(el);
        };
    }, [el]);

    document.body.appendChild(component);
    try {
        setTimeout(() => {
            const el = component.firstChild;
            console.log('Hover:', forceTheme, enableBurst, customStaticBg);
            // Expect the background to be set correctly
        }, 1000);
    } catch (error) {
        console.error('Error:', error);
    }
    document.body.removeChild(component);
}

```

 --- 

## glowHoverEffect

### Description


The glowhover effect provides a visual enhancement to an element's hover state by adding a subtle glow animation around its boundaries. It is commonly used in web applications for various elements such as buttons, cards, and navigation links to improve user experience.
### Parameters

#### el

##### Type


HTMLElement
##### Description


The element to apply the glow hover effect on.

 --- 

#### preset

##### Type


string
##### Description


Preset configuration name. If omitted, uses default configuration from 'glow' preset.

 --- 

#### lightColor

##### Type


string
##### Description


Custom color for the light effect. Use with care as it can conflict with theme colors.

 --- 

#### forceTheme

##### Type


boolean | 'light' | 'dark'
##### Description


Forces a theme-dependent glow animation when active. This is an advanced option and should be used sparingly.
### Return Value

#### Function

##### Type


(void)
##### Description


Returns void after applying the glow effect to the specified element during hover.
### Example Use
```ts 
function example() {
  return document.querySelector('button').useGlowHover({
    lightColor: '#ff0000',
    forceTheme: true
  });
}
example().
```
### Test Cases

#### Basic GlowHoverUsage

##### Description


Tests the basic usage of glowhover with default settings.
##### Code
```ts 
function test() {
  const el = document.querySelector('button');
  return useGlowHover(el);
}
test().check(None); // Verify no errors occurred during the setup.
```

 --- 

#### Custom Preset

##### Description


Tests using a custom preset configuration.
##### Code
```ts 
function test() {
  const el = document.querySelector('a');
  return useGlowHover(el, 'customPreset');
}
test().check(None);

```

 --- 

#### Force Theme

##### Description


Tests if force theme option works as intended.
##### Code
```ts 
function test() {
  const el = document.querySelector('div');
  return useGlowHover(el, {forceTheme: 'dark'});
}
test().check(None);

```

 --- 

#### Light Color Customization

##### Description


Tests the light color customization.
##### Code
```ts 
function test() {
  const el = document.querySelector('p');
  return useGlowHover(el, {lightColor: '#ffff00'});
}
test().check(None);

```

 --- 

## GlowHoverOptions

### Description


The GlowHoverEffect provides a visual enhancement to elements by adding a subtle glow effect on hover. It's designed to be used with React hooks and can be customized through various parameters to adjust the glow's appearance and animation timing.
### Parameters

#### hoverBg

##### Type


string | undefined
##### Description


Sets the background color of the element when hovered. If not provided, default colors from the preset are used.

 --- 

#### lightSize

##### Type


number | undefined
##### Description


Determines the size of the glow effect. A larger number increases the glow intensity.

 --- 

#### lightSizeEnterAnimationTime

##### Type


number | undefined
##### Description


Sets the animation time for the light to appear when entering the hover state. Defaults to 200ms if not provided.

 --- 

#### lightSizeLeaveAnimationTime

##### Type


number | undefined
##### Description


Sets the animation time for the light to disappear when leaving the hover state. Defaults to 400ms if not provided.

 --- 

#### isElementMovable

##### Type


boolean
##### Description


If true, enables the glow effect on hover; if false, disables it.

 --- 

#### customStaticBg

##### Type


string | undefined
##### Description


Custom static background color when hovering. If provided, overrides the default behavior.

 --- 

#### forceTheme

##### Type


string | boolean
##### Description


Forces a specific light/dark theme on the element during hover. Can be 'light', 'dark', or false (disabled).

 --- 

#### enableBurst

##### Type


boolean
##### Description


Enables an additional burst effect when hovering. When true, adds a quick flash of light.

 --- 

#### mode

##### Type


string | undefined
##### Description


Sets the glow animation mode to either 'glow' for smooth transitions or 'sharp' for abrupt changes. Defaults to 'glow'.
### Return Value

#### Function

##### Type


(el: HTMLElement) => void
##### Description


The effect function that is called when the element enters hover, modifying its visual properties.
### Example Use
```ts 
function ExampleUse() {
  const el = document.createElement('div');
  el.style.backgroundColor = '#f0f0f0';
  useGlowHover(el, { ...defaultOptions, lightSize: 30, forceTheme: 'light' });
 }
```
### Test Cases

#### Basic Glow Hover

##### Description


Tests the basic functionality of the glow hover effect with default settings.
##### Code
```ts 
function test() {
  const el = document.createElement('div');
  el.style.backgroundColor = '#f0f0f0';
  useGlowHover(el);
 }
```

 --- 

#### Custom Glowing

##### Description


Tests customizing the glow parameters.
##### Code
```ts 
function test() {
  const el = document.createElement('div');
  el.style.backgroundColor = '#f0f0f0';
  useGlowHover(el, { lightSize: 40, lightSizeEnterAnimationTime: 150 });
 }
```

 --- 

#### Force Theme

##### Description


Tests enabling the force theme during hover.
##### Code
```ts 
function test() {
  const el = document.createElement('div');
  el.style.backgroundColor = '#f0f0f0';
  useGlowHover(el, { forceTheme: 'dark' });
 }
```

 --- 

#### Burst Effect

##### Description


Tests the enableBurst option for a burst effect.
##### Code
```ts 
function test() {
  const el = document.createElement('div');
  el.style.backgroundColor = '#f0f0f0';
  useGlowHover(el, { enableBurst: true });
 }
```

 --- 

#### Mode Testing

##### Description


Tests the mode parameter to switch between 'glow' and 'sharp' effects.
##### Code
```ts 
function test() {
  const el = document.createElement('div');
  el.style.backgroundColor = '#f0f0f0';
  useGlowHover(el, { mode: 'sharp' });
 }
```