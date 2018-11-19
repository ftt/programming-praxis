struct Trie {
    children: Vec<TrieNode>,
}

struct TrieNode {
    letter: char,
    is_word_end: bool,
    children: Vec<TrieNode>,
}

impl TrieNode {
    fn new(letter: char, is_word_end: bool) -> TrieNode {
        TrieNode {
            letter: letter,
            is_word_end: is_word_end,
            children: Vec::new(),
        }
    }
}

impl Trie {
    fn new() -> Trie {
        Trie {
            children: Vec::new(),
        }
    }
}

#[cfg(test)]
mod tests {
    use ::{Trie, TrieNode};

    #[test]
    fn it_works() {
        let trie = Trie::new();
        let trie_node = TrieNode::new('a', true);
    }
}
