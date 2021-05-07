package main

import (
	"fmt"
	"log"
	"net/http"
	"unicode/utf8"
)

var port string = ":8080"

func trimFirstRune(s string) string {
	_, i := utf8.DecodeRuneInString(s)
	return s[i:]
}

func main() {
	http.HandleFunc("/hello-world", func (w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hello world"))
	})

	fmt.Printf("Starting server at port %s\n", trimFirstRune(port))
 	if err := http.ListenAndServe(port, nil); err != nil {
		 log.Fatal(err)
	 }
}