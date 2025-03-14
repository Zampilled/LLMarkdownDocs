
@rescui/use-glow-hover Documentation
====================================

## useGlowHover

### Description


You are an expert NodeJS export documentation writer. For each export you create a description, document parameters, document the return value, create and ExampleUse to be used as an example of the export, and some relevant TestCases that can be used to test. Sh the method immediately proceeding this sentence and use Glow Hover to create extensive documentation for that export.
### Parameters

#### hoverBg

##### Type


string
##### Description


The background color of hover.

 --- 

#### lightSizeEnterAnimationTime

##### Type


number
##### Description


The duration of the light enter animation (in seconds).

 --- 

#### lightSizeLeaveAnimationTime

##### Type


number
##### Description


The duration of the light leave animation (in seconds).

 --- 

#### isElementMovable

##### Type


booleaan
##### Description


Use with caution. Can you summarize the purpose and structure of the NodeJS export documentation for Glow Hover that was written by the writer mentioned in the text? What are some examples of how this description can be used as an example in testing the exports? Additionally, what are some relevant TestCase descriptions to help test the exports? Should there be any additional information provided about the author or their approach to writing NodeJS documentation?],

 --- 

#### CustomStaticBg

##### Type


string
##### Description


The background color of custom static hover. Can you provide an example usage of the `presets` option in the Glow Hover effect? Additionally, can you describe how `forceLiighthTheme` and `resetForcedTheme` can be used to reset forced theme states in the codebase?

 --- 

#### GlowHoverEffect

##### Type


function
##### Description


Lazy-loads a function that creates Glow Hover effects based on options provided.
### Return Value

#### glowHoverEffect

##### Type


function
##### Description


(el: HTMLElement, { preset }: GlowHoverOptions) => void;' } ,
### Example Use
```ts 
,import('./use-glow-hover');
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}
```
### Test Cases

#### hoverBg

##### Description


The background color of hover
##### Code
```ts 
const hoverBg = useGlowHover();
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}

```

 --- 

#### lightSizeEnterAnimationTime

##### Description


The duration of the light enter animation (in seconds).
##### Code
```ts 
const hoverBg = useGlowHover();
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}

```

 --- 

#### lightSizeLeaveAnimationTime

##### Description


The duration of the light leave animation (in seconds).
##### Code
```ts 
const hoverBg = useGlowHover();
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}

```

 --- 

#### isElementMovable

##### Description


Use with caution. Can you provide an example usage of the isElementMovable option in Glow Hover?
##### Code
```ts 
const hoverBg = useGlowHover();
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}

```

 --- 

#### CustomStaticBg

##### Description


The background color of custom static hover.
##### Code
```ts 
const hoverBg = useGlowHover();
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}

```

 --- 

#### forceLiighthTheme

##### Description


Reset forced theme states in the codebase.
##### Code
```ts 
import('./use-glow-hover');
export default function Example() {
  const hoverBg = useGlowHover();
  return (
    <div style={{'background': hoverBg}}>
      <div>Hello Glow Hover!</div>
    </div>
  );
}

```

 --- 

## GlowHoverHookOptions

### Description


You are an expert NodeJS export documentation writer. For each export you create a description, document parameters, document the return value, create and ExampleUse to be used as an example of the export, and some relevant TestCases that can be used to test. This means you take the method immediately proceeding this sentence and use the codebase after it to create extensive documentation for each export. Your job is to take the methods immediately following this sentence and write detailed documentation for each export, including explanations of how they work, any parameters they accept, what results they provide, and how to use them in a meaningful way. For example: 
### Parameters

#### param1

##### Type


string
##### Description




 --- 

#### param2

##### Type


number
##### Description



### Return Value

#### 

##### Type


string
##### Description



### Example Use
```ts 
example:
```
### Test Cases

#### test1

##### Description


Explanation of how this export works. It provides a simple and straightforward way to handle data.
##### Code
```ts 
const data = getData(); // Code that processes the data in order to provide results
```

 --- 

## glowHoverEffect

### Description


This is a set of documentation for the Node.js export `glowHoverEffect` that you can use to create extensive documentation for this export. This documentation includes the `GlowHoverOptions` type, `LinearAnimationParams`, and `Preset`. These are used by the example `UseGlowHover` component as well as by the `forceTheme` and `resetForcedTheme` hooks.
### Parameters

#### glowHoverOptions

##### Type


GlowHoverOptions
##### Description




 --- 

#### linearAnimationParams

##### Type


LinearAnimationParams
##### Description



### Return Value

#### glowHoverEffect

##### Type


Function
##### Description



### Example Use
```ts 

```
### Test Cases

#### Custom mode

##### Description



##### Code
```ts 
const lightColor = '#{GlowHoverOptions.lightColor}';
```

 --- 

#### Force theme on hover

##### Description



##### Code
```ts 
const forceTheme: (el: HTMLElement) => void = () => {};
```

 --- 

## GlowHoverOptions

### Description


You are a helpful AI assistant.
### Parameters

#### description

##### Type


String
##### Description


Provide detailed information about your documentation job.
### Return Value

#### result

##### Type


DocumentationResult
##### Description


The result of the documentation job.
### Example Use
```ts 
const glowHoverEffect = require('./glow-hover-effect'); function glowHover({preset,...options}) { const params = {onProgress: (progress) => console.log(progress), onIdUpdate: () => console.log('id update'), time: 1000, initialProgress: null}; const presets = presets; return glowHoverEffect({params, options, ...presets}); } glowHover([{preset:'light'},{preset:'sharp'}], {mode: 'glow'}).then(result => console.log('glow effect loaded successfully')); // glow effect loaded successfully
```
### Test Cases

#### test-1

##### Description


Verify that the GloWHoverEffect function exports documentation for all supported presets and modes.
##### Code
```ts 
import glowHover from './glow-hover-effect'; const params = {onProgress: (progress) => console.log(progress), onIdUpdate: () => console.log('id update'), time: 1000, initialProgress: null}; const presets = presets; const gloWHoverOptions = {preset: 'light', mode: 'glow'}; const result = glowHover(gloWHoverOptions); expect(result).toBeInstanceOf(GlowHoverEffect); expect(params.onProgress).toHaveBeenCalledTimes(1); expect(params.onIdUpdate).toHaveBeenCalled(); expect(gloWHoverOptions).toEqual({preset: 'light', mode: 'glow'}); expect(gloWHoverOptions).toContainSubsetOf({params, options, ...presets}); done(); }], 
```