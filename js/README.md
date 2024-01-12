# nh5 JavaScript library

nh5 is a JavaScript package that provides tools for efficiently reading data from remote .nh5 files in web applications. This package exposes the RemoteNh5FileClient class.

See also the [nh5 Python package](https://github.com/magland/nh5).

## Installation

```
yarn add nh5
# or
npm install nh5
```

## Usage

The RemoteNh5FileClient class is used to interact with NH5 files hosted remotely. Here's an example usage in a React application.

```typescript
import { RemoteNh5FileClient } from 'nh5';

...

const useNh5FileClient = (nh5Url?: string) => {
  const [client, setClient] = useState<RemoteNh5FileClient | undefined>(undefined)
  useEffect(() => {
      let canceled = false
      if (!nh5Url) return
      ; (async () => {
          const c = await RemoteNh5FileClient.create(nh5Url)
          if (canceled) return
          setClient(c)
      })()
      return () => {canceled = true}
  }, [nh5Url])
  return client
}

...

const MyComponent = () => {
  const nh5Url = 'path_to_your_nh5_file.nh5' // Replace with your NH5 file URL
  const client = useNh5FileClient(nh5Url)

  useEffect(() => {
    async function load() {
      if (!client) return
      const rootGroup = await client.getGroup('/')
      console.log('Root group:', rootGroup)

      const dataset = await client.getDataset('/dataset_path')
      console.log('Dataset:', dataset)

      const data = await client.getDatasetData('/dataset_path', {})
      console.log('Data:', data)

      // other options including slicing are also supported
    }
    load()
  }, [client])

  if (!client) return <div>Loading...</div>
  return (
    <div>
      ...
    </div>
  )
}
```

## Contributing

Contributions to the nh5 package are welcome. Please feel free to submit issues and pull requests.

## License

The code in this project is licensed under Apache License 2.0.

## Author

The package and format were created by Jeremy Magland.