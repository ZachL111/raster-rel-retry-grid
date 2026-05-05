// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../src/PolicyScore.sol";

contract PolicyScoreTest {
    function test_case_1() public pure {
        PolicyScore scorer = new PolicyScore();
        PolicyScore.Signal memory signal = PolicyScore.Signal(56, 73, 22, 7, 8);
        require(scorer.score(signal) == 147, "score mismatch");
        require(scorer.accepted(signal) == false, "decision mismatch");
    }
    function test_case_2() public pure {
        PolicyScore scorer = new PolicyScore();
        PolicyScore.Signal memory signal = PolicyScore.Signal(89, 104, 12, 16, 4);
        require(scorer.score(signal) == 186, "score mismatch");
        require(scorer.accepted(signal) == true, "decision mismatch");
    }
    function test_case_3() public pure {
        PolicyScore scorer = new PolicyScore();
        PolicyScore.Signal memory signal = PolicyScore.Signal(105, 102, 19, 20, 13);
        require(scorer.score(signal) == 232, "score mismatch");
        require(scorer.accepted(signal) == true, "decision mismatch");
    }
}
