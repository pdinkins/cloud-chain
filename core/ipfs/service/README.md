To try it out, run the following on one computer:
```
$ ipfs init # if you havent already
$ go run host.go
```
That should print out that peers ID, copy it and use it on a second machine:
```
$ ipfs init # if you havent already
$ go run client.go <peerID>
```
It should print out Hello! This is whyrusleepings awesome ipfs service

Now, you might be asking yourself: “Why would I use this? How is it better than the net package?“. Well, here are the advantages:
1. You dial a specific peerID, no matter what their IP address happens to be at the moment.
2. You take advantage of the NAT traversal built into our net package.
3. Instead of a ‘port’ number, you get a much more meaningful protocol ID string.

By [whyrusleeping](https://github.com/whyrusleeping)
- [IPFS_DOCS](https://docs.ipfs.io/guides/examples/api/service/readme/)