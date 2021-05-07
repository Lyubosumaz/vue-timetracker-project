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

func helloHandler(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/hello-world" {
        http.Error(w, "404 not found.", http.StatusNotFound)
        return
    }

    if r.Method != "GET" {
        http.Error(w, "Method is not supported.", http.StatusNotFound)
        return
    }

	w.Write([]byte("Hello World!!"))
}

func main() {
	http.HandleFunc("/hello-world", helloHandler)

	fmt.Printf("Starting server at port %s\n", trimFirstRune(port))
 	if err := http.ListenAndServe(port, nil); err != nil {
		 log.Fatal(err)
	 }
}